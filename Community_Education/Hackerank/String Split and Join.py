def split_and_join(line):
    # write your code here
    
    words = line.split(" ")
    
    joinedString = "-".join(words)
    
    return joinedString

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
