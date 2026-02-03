# Security Scanner

A security scanner that detects vulnerabilities using Semgrep.

## Installation
```bash
git clone https://github.com/ishak-arif/Security-Scanner.git
cd security-scanner
pip3 install -r requirements.txt
```

## Usage
- Edit main.py and change the target file:
```python
target = "your_file.py"
```
- Run the scanner:
```bash
python3 main.py
```

## Roadmap
- [ ] Add Typer for improved CLI.
- [ ] Add Rich for aesthetic terminal output.
- [ ] Add support for scanning multiple files.
- [ ] Export results to JSON/HTML reports.
- [ ] Add GUI interface.