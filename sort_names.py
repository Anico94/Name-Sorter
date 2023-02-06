from person import Person

class SortNames:
  """
  Class that sorts names
  """

  def sort_by_last_name(self, list_of_names):

    # Initilise a list of that will hold people created from the Person class
    names_of_people = []
    
    for name in list_of_names:
      names_of_people.append(Person(name))
    
    #list of people sorted by last name
    sorted_by_last_name = sorted(names_of_people, key=lambda person: (person.last_name, person.given_names))

    # create a list of names(strings) from the sorted people list
    sorted_names_by_last_name = []

    for name in sorted_by_last_name:
      sorted_names_by_last_name.append(name.name)

    return sorted_names_by_last_name  

