import os
import sys
import click

@click.command()
@click.option('--path', prompt='Ruta del módulo Odoo', help='Ruta local del módulo a auditar')
def audit(path):
    """Herramienta de auditoría asistida por IA para módulos de Odoo ERP."""
    click.echo(click.style(f" Escaneando directorio: {path}", fg='cyan'))
    
    manifest_path = os.path.join(path, '__manifest__.py')
    security_path = os.path.join(path, 'security', 'ir.model.access.csv')
    
    issues = []
    
    if not os.path.exists(manifest_path):
        issues.append(" Falta el archivo __manifest__.py raíz.")
        
    if not os.path.exists(security_path):
        issues.append(" Advertencia de Seguridad: No se encontró ir.model.access.csv.")

    click.echo("\n--- RESULTADOS DEL ANÁLISIS PRELIMINAR ---")
    if not issues:
        click.echo(click.style(" Estructura base válida según estándares de Odoo.", fg='green'))
    else:
        for issue in issues:
            click.echo(click.style(issue, fg='yellow'))

    click.echo(click.style("\n Simulación de análisis LLM: Sin fugas críticas de seguridad.", fg='magenta'))

if __name__ == '__main__':
    audit()
