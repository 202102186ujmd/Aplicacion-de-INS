class CustomPasswordResetView(PasswordResetView):
    template_name = 'registration/password_reset.html'
    html_email_template_name = 'registration/password_reset_email.html'  # Solo la plantilla HTML
    success_url = reverse_lazy('password_reset_done')
    # Aquí puedes agregar más configuraciones si es necesario 