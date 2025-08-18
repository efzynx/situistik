# cli.py

import typer
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich import print

# Impor fungsi utama dari file checker.py kita
from checker import run_all_checks

# Inisialisasi aplikasi Typer dan konsol Rich
app = typer.Typer(add_completion=False)
console = Console()

def print_status_panel(status_data: dict):
    """Menampilkan panel status yang rapi."""
    if status_data.get('up'):
        status_emoji = ":white_check_mark:"
        panel_color = "green"
        status_text = f"[bold]UP[/bold] (Status: {status_data['status_code']} {status_data['reason']})"
    else:
        status_emoji = ":x:"
        panel_color = "red"
        status_text = f"[bold]DOWN[/bold]\nReason: {status_data['reason']}"
        
    final_url = status_data.get('url', 'N/A')
    
    print(Panel(
        f"{status_emoji} {status_text}\nURL Final: {final_url}",
        title="[bold]Website Status[/bold]",
        border_style=panel_color,
        padding=(1, 2)
    ))

def print_dns_table(dns_data: dict):
    """Menampilkan record DNS dalam format tabel."""
    table = Table(title="[bold]DNS Records[/bold]")
    table.add_column("Tipe Record", style="cyan", no_wrap=True)
    table.add_column("Nilai", style="magenta")

    for record_type, values in dns_data.items():
        if values:
            # Gabungkan beberapa nilai menjadi satu string dengan baris baru
            value_str = "\n".join(values)
            table.add_row(record_type, value_str)
    
    console.print(table)

def print_whois_panel(whois_data: dict):
    """Menampilkan informasi Whois dalam panel."""
    if 'error' in whois_data:
        content = f"[red]Tidak bisa mengambil data Whois: {whois_data['error']}[/red]"
    else:
        content = (
            f"[bold]Registrar:[/bold] {whois_data.get('registrar')}\n"
            f"[bold]Dibuat pada:[/bold] {whois_data.get('creation_date')}\n"
            f"[bold]Kadaluarsa pada:[/bold] {whois_data.get('expiration_date')}"
        )
    
    print(Panel(
        content,
        title="[bold]Whois Information[/bold]",
        border_style="yellow",
        padding=(1, 2)
    ))


@app.command()
def analyze(
    domain: str = typer.Argument(..., help="Domain yang ingin dianalisis. Contoh: google.com")
):
    """
    Analisis lengkap sebuah domain: status, DNS, dan Whois.
    """
    with console.status(f"[bold green]Menganalisis {domain}...[/]", spinner="dots"):
        results = run_all_checks(domain)

    console.rule(f"[bold]Laporan Analisis untuk {domain}[/bold]", style="blue")
    
    # Cetak setiap bagian dengan format yang cantik
    print_status_panel(results['status_check'])
    print_whois_panel(results['whois_info'])
    print_dns_table(results['dns_records'])
    
    console.print(f"\n:stopwatch:  Analisis selesai pada: {results['checked_at']}")


if __name__ == "__main__":
    app()