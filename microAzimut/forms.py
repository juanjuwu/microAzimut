from django import forms


##class Calculo(forms.Form):
##    P1=forms.BooleanField(label="P1")

DISPLAY_CHOICES = (
    ("P1", "High detection of failed host"),
    ("P2", "Intermittently asynchronous data transmission"),
    ("P4","Efficient duration of timeouts periods"),
    ("P5","High isolation"),
    ("P6","Effective load balancing"),
    ("P7","Quick broken state recovery"),
            
    ("P8","High control of failure propagation"),
            
    ("P9","High service monitoring visibility"),
            
    ("P10","Periodic heartbeat signal"),
            
    ("P11","Low application restarting"),
            
    ("P12","Efficient resources consumption"),
    ("S1","Effective technical duplication"),
            
    ("S2","High functional decomposition"),
            
    ("S3","Effective data partitioning"),
      
        
        
        
    ("I1","High cooperation among components"),
            
    ("I2","High coordinated orchestration among components"),
    ("C1","Strong level of individuals, groups, or systems authorization"),
            
    ("C2","High-security authentication"),
            
    ("C3","Effective credentials management"),
            
    ("C4","Effective access control")
      
)

class MyForm(forms.Form):
   display_type = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=DISPLAY_CHOICES)

# class MyForm(forms.Form):
#     # For BooleanFields, required=False means that Django's validation
#     # will accept a checked or unchecked value, while required=True
#     # will validate that the user MUST check the box.
#     something_truthy = forms.BooleanField(required=True)