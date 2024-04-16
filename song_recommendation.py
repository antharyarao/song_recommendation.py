print("WELCOME TO OUR SONG RECOMMENDATION SYSTEM\n")

Songs=["song1","song2","song3"]

print("SONGS:-\n")
print(Songs)
print("\n")

while(True):
	g=input("Enter your genre:")
	Genre={
	"Happy":"song1",
	"Sad":"song2",
	"K-pop":"song3"
	}
	
	Yes="y"
	No="n"
	if g=="Happy":
		print("Your happy song is",Genre["Happy"])
		print("Put only y or n:-")
		Ask=input("Do you want to exit Yes/No:")
		if Ask=="y":
			break
			
	elif g=="Sad":
		print("Your sad song is",Genre["Sad"])
		print("Put only y or n:-")
		Ask=input("Do you want to exit Yes/No:")
		if Ask=="y":
			break
			
	elif g=="K-pop":
		print("Your K-pop song is",Genre["K-pop"])
		print("Put only y or n:-")
		Ask=input("Do you want to exit Yes/No:")
		if Ask=="y":
			break
			
	else:
		print("Your search is not found")
		print("Thanks for your feedback")
		print("Put only y or n:-")
		Ask=input("Do you want to exit Yes/No:")
		if Ask=="y":
			break

