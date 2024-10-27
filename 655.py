def capitalize_every_words_in_sentence(sentence: str):
    capitalized_sentence = ""
    for i in range(len(sentence)):
        if i == 0:
            capitalized_sentence += sentence[i].upper()
        elif sentence[i-1] == " ":
            capitalized_sentence += sentence[i].upper()
        else:
            capitalized_sentence += sentence[i].lower()
    return capitalized_sentence


if __name__ == "__main__":
    number_of_movies = input(" enter number of movies :")
    movies_list = []
    for i in range(int(number_of_movies)):
        movies_list.append(input(" enter your movie's name:"))

    for movie in movies_list:
        print(capitalize_every_words_in_sentence(movie))
