from  django import template
from  django.utils.html import format_html
from  django.conf import  settings
from django.template.defaultfilters import stringfilter
import math
register=template.Library()

@register.simple_tag()
def outputpage(page):
    pagenum=getattr(settings,"SHOW_MUCH_PAGE",6)
    middlenum=math.ceil(int(pagenum)/2)
    addpage=math.ceil(int(pagenum)/2)
    # middlenum=int(middlenum)
    # addpage=int(addpage)
    total=int(page.paginator.num_pages)
    current=int(page.number)
    print total
    if total<pagenum:
        start=1
        end=total
    else:
        if current < middlenum:
            start=1
            end=pagenum
        else:

            if ( current + addpage) > total:
                star = total - addpage
                end = total
            else:
                star = current + addpage
                end = current - addpage
    if current == 1:
        firdisable="paginate_button_disabled"
        firhref=""
    else:
        firdisable=''
        firhref="href='?page=1'"

    if current==total:
        enddisable="paginate_button_disabled"
        endhref=""
    else:
        enddisable=''
        endhref="href='?page=%s'"%str(total)

    if page.has_next():
        nextdisable=""
        nexthref="href='?page=%s'"%str(current+1)
    else:
        nextdisable='paginate_button_disabled'
        nexthref=''

    if page.has_previous():
        prevdisable=""
        prevhref = "href='?page=%s'"%str(current-1)
    else:
        prevdisable='paginate_button_disabled'
        prevhref=''



    htmlstr="<div class ='dataTables_info' id='DataTables_Table_2_info'> Showing 1 to 5 of 10 entries </div >"
    htmlstr+="<div class ='dataTables_paginate paging_full_numbers' id='DataTables_Table_2_paginate'> "

    htmlstr+="<a "+firhref+" tabindex='0' class='first paginate_button "+firdisable+"' id='DataTables_Table_2_first' >First</a>"


    htmlstr+="<a "+prevhref+" tabindex='0' class ='previous paginate_button "+prevdisable+"' id='DataTables_Table_2_previous'> Previous </a>"
    htmlstr+="<span>"
    for i in range(start,end+1):
        if i== current:
            active='paginate_button_disabled'
            href=''
        else:
            active=""
            href="href='?page=%s'"%str(i)
        htmlstr+="<a tabindex='0' "+href+" class='paginate_active "+active+"' > "+str(i)+"</a>"
    htmlstr+="</span> "
    htmlstr+="<a "+nexthref+" tabindex='0' class ='next paginate_button "+nextdisable+"' id='DataTables_Table_2_next' > Next </a>"
    htmlstr+="<a "+endhref+" tabindex='0' class ='last paginate_button "+enddisable+"' id='DataTables_Table_2_last'> Last </a>"
    htmlstr+="</div>"

    return format_html(htmlstr)

@register.filter
@stringfilter
def strip(value,tag):
    value=value.strip()
    return  value.strip(tag)


