def caesar_encrypt(text,shift):
       result=" "
       for char in text:
          if char.isupper():
              result += chr((ord(char) - 65 + shift) % 26 + 65)
          elif char.islower():
              result +=chr((ord(char) - 97 + shift)% 26 +  97)
          else :
              result+= char
       return result


def caesar_decrypt(text,shift):
        return caesar_encrypt(text,-shift)
def main():

  print("====Caesar cypher=====\n")
  choice=input("Do  you want to encrypt(e) or decrypt(d)? ") 
  message= input("\nEnter the message you want ....")
  shifts=int(input("\nEnter the number of shift you want..."))
  if choice == 'e' :

      results=caesar_encrypt(message,shifts)
      print("\nYour message before encrypion ",message)
      print("\nYour message after encrypion ",results)
  elif choice =='d' :
     results=caesar_decrypt(message,shifts)
     print("\nYour message before decrypion ",message)
     print("\nYour message after decrypion ",results)
  else :
     print("Enter a valid choice")
     
if __name__ == "__main__":
    main()
