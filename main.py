import typer
from rich.console import Console
from rich.table import Table
from reddit_monitor import RedditMonitor
from csv_exporter import export_to_csv

app = typer.Typer()
console = Console()

@app.command()
def monitor(
    subreddit: str = typer.Option(..., "--subreddit", "-s", help="Subreddit to monitor"),
    keywords: str = typer.Option("looking for,need help,recommend,suggestion", "--keywords", "-k", help="Comma-separated keywords"),
    limit: int = typer.Option(50, "--limit", "-l", help="Number of posts to check"),
    output: str = typer.Option("leads.csv", "--output", "-o", help="Output CSV file"),
):
    """Monitor Reddit for potential customer leads based on buying intent keywords"""
    console.print(f"[bold green]Monitoring r/{subreddit}...[/bold green]")
    
    keyword_list = [k.strip() for k in keywords.split(",")]
    console.print(f"Keywords: {', '.join(keyword_list)}")
    
    monitor = RedditMonitor()
    leads = monitor.scan_subreddit(subreddit, keyword_list, limit)
    
    if leads:
        table = Table(title=f"Found {len(leads)} Leads")
        table.add_column("Username", style="cyan")
        table.add_column("Type", style="magenta")
        table.add_column("Preview", style="yellow")
        
        for lead in leads[:10]:
            preview = lead['content'][:60] + "..." if len(lead['content']) > 60 else lead['content']
            table.add_row(lead['username'], lead['type'], preview)
        
        console.print(table)
        
        export_to_csv(leads, output)
        console.print(f"[bold green]Exported {len(leads)} leads to {output}[/bold green]")
    else:
        console.print("[yellow]No leads found[/yellow]")

if __name__ == "__main__":
    app()
