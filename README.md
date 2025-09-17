# Quasar: Markdown to html and database creator

Jul.2025 - 

## with 'pip install markdown'

### Memo
1. python3 -m venv .env
2. source .env/bin/activate
3. pip install markdown

## Sequence Diagram
```mermaid
 sequenceDiagram
    loop Every Directory
        activate main
        main->>main: os.listdir(path.MARKDOWN)
        main->>db_controller: select_col_dir
        activate db_controller
        db_controller->>main: result
        deactivate db_controller
        main->>v_and_v: verify_dir
        activate v_and_v
        v_and_v->>main: TYPE.VERIFIED
        deactivate v_and_v
        main->>v_and_v: validate_dir
        activate v_and_v
        v_and_v->>v_and_v: os.listdir(path.MARKDOWN/directory)
        v_and_v->>db_controller: select_dir
        activate db_controller
        db_controller->>db_manager: select_query
        activate db_manager
        db_manager->>db_controller: result
        deactivate db_manager
        db_controller->>v_and_v: result
        deactivate db_controller
        v_and_v->>v_and_v: verify_file
        alt result is None
            v_and_v->>db_controller: insert_dir
            activate db_controller
            db_controller->>db_manager: insert_query
            activate db_manager
            db_manager->>db_controller: result
            deactivate db_manager
            db_controller->>v_and_v: result
            deactivate db_controller
            v_and_v->>main: TYPE.VALID
        else result is NOT None
            v_and_v->>main: TYPE.VALID
            deactivate v_and_v
        end
        main->>main: os.listdir(path.MARKDOWN/directory)
        loop Every File
        	main->>db_controller: select_all_files
        	activate db_controller
        	db_controller->>main: result
        	deactivate db_controller
            main->>v_and_v: verify_file
            activate v_and_v
            v_and_v->>main: TYPE.VERIFIED
            deactivate v_and_v
            main->>data_pipe: set_file_info
            activate data_pipe
            data_pipe->>data_manager: GET
            activate data_manager
            data_manager->>data_pipe: SET
            deactivate data_manager
            data_pipe->>main: data_store
            deactivate data_pipe
            main->>v_and_v: valid_file
            activate v_and_v
            v_and_v->>db_controller: select_file
            activate db_controller
            db_controller->>db_manager: select_query
            activate db_manager
            db_manager->>db_controller: result
            deactivate db_manager
            db_controller->>v_and_v: result
            deactivate db_controller
            alt result is None
                v_and_v->>main: Type.NEW
            else result.revised_time != file.revised
                v_and_v->>main: Type.UPDATE
            else
                v_and_v->>main: Type.NOACTION
                deactivate v_and_v
            end
            alt valid_id == Type.NEW
                main->>md_changer: convert_md_to_html
                activate md_changer
                md_changer->>main: TYPE.SUCCESS
                deactivate md_changer
                main->>db_controller: insert_new_file
                activate db_controller
                db_controller->>db_manager: insert_query
                activate db_manager
                db_manager->>db_controller: result
                deactivate db_manager
                db_controller->>main: result
                deactivate db_controller
            else valid_id == Type.UPDATE
                main->>md_changer: convert_md_to_html
                activate md_changer
                md_changer->>main: TYPE.SUCCESS
                deactivate md_changer
                main->>db_controller: update_file
                activate db_controller
                db_controller->>db_manager: update_query
                activate db_manager
                db_manager->>db_controller: ?
                deactivate db_manager
                db_controller->>main: ?
                deactivate db_controller
            end
        end
        deactivate main
    end
```
