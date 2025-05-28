from django import forms
from .models import Document, DocumentType

class DocumentUploadForm(forms.ModelForm):
    """Form for uploading documents"""
    
    class Meta:
        model = Document
        fields = ['document_type', 'title', 'file', 'notes', 'expiry_date']
        widgets = {
            'document_type': forms.Select(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'file': forms.FileInput(attrs={'class': 'form-control', 'accept': '.pdf,.jpg,.jpeg,.png'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'expiry_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['expiry_date'].required = False
        self.fields['notes'].required = False
    
    def clean_file(self):
        file = self.cleaned_data.get('file')
        document_type = self.cleaned_data.get('document_type')
        
        if file and document_type:
            # Check file size
            if file.size > document_type.max_file_size:
                raise forms.ValidationError(
                    f'File size too large. Maximum size is {document_type.max_file_size/1024/1024:.1f}MB'
                )
            
            # Check file extension
            allowed_extensions = document_type.allowed_extensions.split(',')
            file_extension = file.name.split('.')[-1].lower()
            
            if file_extension not in allowed_extensions:
                raise forms.ValidationError(
                    f'File type not allowed. Allowed types: {", ".join(allowed_extensions)}'
                )
        
        return file