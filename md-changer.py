import os
import markdown
import path

#List direcories up
dir_list=os.listdir(path.MARKDOWN)

dir_count = 1
for directory in dir_list:

    if(directory == path.GIT):
        continue
    
    #List files in a directory up
    file_list=os.listdir(f"{path.MARKDOWN}/{directory}")
    
    file_count = 1
    for file in file_list:
        extension = list(os.path.splitext(file))
        if(extension[1].lower() == '.md'):
            # Read Markdown from file
            with open(f"{path.MARKDOWN}/{directory}/{file}", "r", encoding="utf-8") as md_file:
                markdown_content = md_file.read()
                # Convert to HTML
            html_content = markdown.markdown(markdown_content)

            if not os.path.isdir(f"{path.HTMLS}/{directory}"):
                os.mkdir(f"{path.HTMLS}/{directory}")

            # Save HTML to file
            with open(f"{path.HTMLS}/{directory}/{extension[0]}.html", "w", encoding="utf-8", errors="xmlcharrefreplace") as html_file:
                html_file.write(html_content)
            
            print(f"{file} in {directory} has been converted {file_count} / {len(file_list)}")
            file_count += 1

    print(f"{directory} has been completed. {dir_count} / {len(dir_list)}")
    dir_count += 1

print("Markdown converted and saved to output.html")
