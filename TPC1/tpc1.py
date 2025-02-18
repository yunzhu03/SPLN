def main():
    
    different_lines = set()
    result = ""
    
    filename = input("Indique o nome do ficheiro:")
    
    f = open(filename, "r")
    
    for line in f:
        if line not in different_lines:
            different_lines.add(line)
            result += line
            
    f.close()
    
    print(result)
    
    return 0

if __name__ == "__main__":
    main()
    