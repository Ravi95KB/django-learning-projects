from django import template

register = template.Library()

@register.filter(name='cut') #here name is the name you wanna call in the templates for the defined function.
def cut(value,arg):
    '''This cuts out all the arg from the string'''

    return value.replace(arg,'')

@register.filter(name='palin')
def palindrome(value):
    
    return value[::-1]


#register.filter('cut',cut)   #First argument is the name of the function you want to call in the template,
                            #The next argument is the actual function name.
