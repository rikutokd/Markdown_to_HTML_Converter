import markdown
import sys

# python3 file-converter.py markdown sample.md output.html
print(sys.argv)

if len(sys.argv) <= 3:
    print('command is short.')
else:
    command = sys.argv[1]

    with open(sys.argv[2], 'r') as f:
        contents = f.read()

    if command == 'markdown':
        with open(sys.argv[3], 'w') as f:
            html = markdown.markdown(contents)
            f.write(html)
    
    else:
        print('wrong command')