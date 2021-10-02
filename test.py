#import txt file into python list
with open('data.txt', 'r') as f:  
    data = f.readlines()

#removing "/n" from the end of each line
final = [x[:-1] for x in data]
new_list=[]
#creating list of questining words
ques_word = ["who", "whose", "whom", "what", "when","where", "why", "how", "is", "are", "can", "may", "could", "does", "do", "should"]

#looping through each row of the list
i = 0
while i< len(final):

    temp_list=[]
    test_row=[]
    row = final[i]
    #splitting each word from the sentence
    test_row = row.split(" ")

    #extracting first word of each sentence
    test_on = test_row[0]

    #converting word into lowercase for checking
    test_on.lower()

    temp_list.append(row)

    #checking if the first word is in ques_word and appending Yes or No according to it
    if test_on in ques_word:
        temp_list.append("Yes")
        new_list.append(temp_list)
    else:
        temp_list.append("No")
        new_list.append(temp_list)
    i+=1
  
#creating new txt file to write new list
file = open('new_data.txt', 'w')
for row in new_list:
    #formatting each line before writing to the file
    line = ("{0:<33}{1:>18}".format(row[0],row[1]))
    file.write('%s\n' %line)
file.close





