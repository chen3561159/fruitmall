from  django import template
from  django.utils.html import format_html
from  django.conf import  settings
from django.template.defaultfilters import stringfilter
import math
register=template.Library()

@register.simple_tag
def outputpage(page):
    pagenum=getattr(settings,"SHOW_MUCH_PAGE",6)
    middlenum=math.ceil(int(pagenum)/2)
    addpage=math.floor(int(pagenum)/2)
    total=int(page.paginator.num_pages)
    current=int(page.number)
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
    htmlstr="<div class ='dataTables_info' id='DataTables_Table_2_info'> Showing 1 to 5 of 10 entries </div >"
    htmlstr+="<div class ='dataTables_paginate paging_full_numbers' id='DataTables_Table_2_paginate'> "
    htmlstr+="<a href='?page=1' tabindex='0' class='first paginate_button paginate_button_disabled' id='DataTables_Table_2_first' >First</a>"
    htmlstr+="<a href='?page="+(current-1)+"' tabindex='0' class ='previous paginate_button paginate_button_disabled' id='DataTables_Table_2_previous'> Previous </a>"
    htmlstr+="<span>"
    for i in range(start,end):
       htmlstr+="< a tabindex='0' href='?page="+i+"' class ='paginate_active' > "+i+"</a>"
    htmlstr+="</span> "
    htmlstr+="<a href='?page="+(current+1)+"' tabindex='0' class ='next paginate_button' id='DataTables_Table_2_next' > Next </a>"
    htmlstr+="<a href='?page="+total+"' tabindex='0' class ='last paginate_button' id='DataTables_Table_2_last'> Last </a>"
    htmlstr+="</div>"

    return format_html(htmlstr)

@register.filter
@stringfilter
def strip(value,tag):
    return  value.strip(tag)




