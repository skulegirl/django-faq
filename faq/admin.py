from django.contrib import admin
from .models import Question, Topic


class TopicAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name', 'sort_order']
    list_editable = ['sort_order', ]


class QuestionAdmin(admin.ModelAdmin):
    list_display = ['text', 'topic', 'sort_order', 'updated_by', 'updated_on', 'status', ]
    list_editable = ['sort_order', 'status']
    list_filter = ('topic', 'status')
    fields = ('text', 'answer', 'topic', 'slug', 'status', 'protected', 'sort_order', 'html_answer')
    prepopulated_fields = {'slug': ('text',)}

    def save_model(self, request, obj, form, change):
        '''
        Update created-by / modified-by fields.

        The date fields are upadated at the model layer, but that's not got
        access to the user.
        '''
        # If the object's new update the created_by field.
        if not change:
            obj.created_by = request.user

        # Either way update the updated_by field.
        obj.updated_by = request.user

        # Let the superclass do the final saving.
        return super(QuestionAdmin, self).save_model(request, obj, form, change)


admin.site.register(Question, QuestionAdmin)
admin.site.register(Topic, TopicAdmin)
