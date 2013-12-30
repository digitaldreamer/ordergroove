from django.core.urlresolvers import reverse
from django import forms
from django.forms.util import flatatt
from django.forms.widgets import CheckboxInput
from django.utils.encoding import StrAndUnicode, force_unicode
from django.utils.html import escape, conditional_escape
from django.utils.safestring import mark_safe


class AdminImageWidget(forms.ClearableFileInput):
    template_with_initial = u'<img src="%(image)s"><br/> %(initial_text)s: %(initial)s %(clear_template)s<br />%(input_text)s: %(input)s'

    def render(self, name, value, attrs=None):
        substitutions = {
            'initial_text': self.initial_text,
            'input_text': self.input_text,
            'clear_template': '',
            'clear_checkbox_label': self.clear_checkbox_label,
        }
        template = u'%(input)s'
        substitutions['input'] = super(forms.FileInput, self).render(name, value, attrs)

        if value and hasattr(value, "url"):
            template = self.template_with_initial
            substitutions['initial'] = (u'<a href="%s">%s</a>'
                                        % (escape(value.url),
                                           escape(force_unicode(value))))

            substitutions['image'] = escape(value.url)

            if not self.is_required:
                checkbox_name = self.clear_checkbox_name(name)
                checkbox_id = self.clear_checkbox_id(checkbox_name)
                substitutions['clear_checkbox_name'] = conditional_escape(checkbox_name)
                substitutions['clear_checkbox_id'] = conditional_escape(checkbox_id)
                substitutions['clear'] = CheckboxInput().render(checkbox_name, False, attrs={'id': checkbox_id})
                substitutions['clear_template'] = self.template_with_clear % substitutions

        return mark_safe(template % substitutions)




# from django.contrib.admin.widgets import AdminFileWidget
# from django.utils.translation import ugettext as _
# from django.utils.safestring import mark_safe

# class AdminImageWidget(AdminFileWidget):
    # def render(self, name, value, attrs=None):
        # output = []
        # if value and getattr(value, "url", None):
            # image_url = value.url
            # file_name=str(value)
            # output.append(u' <a href="%s" target="_blank"><img src="%s" alt="%s" /></a> %s ' % (image_url, image_url, file_name, _('Change:')))
        # output.append(super(AdminFileWidget, self).render(name, value, attrs))
        # return mark_safe(u''.join(output))
