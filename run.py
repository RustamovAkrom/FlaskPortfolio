from app import create_app


def main():
    try:
        create_app().run()
        
    except KeyboardInterrupt:
        exit(1)
    
    except Exception as e:
        print(f"Shoudown. program exceptions: {e}")
        exit(1)

if __name__=="__main__":
    main()