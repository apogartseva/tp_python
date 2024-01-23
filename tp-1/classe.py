

### q3

class Date():
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year
    def __eq__(self, date):
        self.day = date.day
        self.month = date.month
        self.year = date.year

    def __lt__(self, date): #returns True if date is lesser than self 
        if (date.year < self.year):
            return True
        if (date.year == self.year):
            if date.month < self.month : 
                return True
            if date.month == self.month :
                if date.day < self.day:
                    return True 
                else: 
                    return False
            else : 
                return False
        else : 
            return False



class Etudiant():
    def __init__(self, nom, prenom, date_de_naissance):
        self.nom = nom
        self.prenom = prenom 
        self.date_de_naissance = date_de_naissance
    def creer_mail(self):
        mail = self.prenom + "." + self.nom + "@etu.univ-tours.fr"
        return mail
    def age(self):
        # date_de_naissace ressemble a "01/01/1970"
        today = date.today()
            # Calculation
        
        years = current_date.year - birth_date.year
        months = current_date.month - birth_date.month
        days = current_date.day - birth_date.day

        # Adjust for negative differences
        if days < 0:
            months -= 1
            days += get_days_in_month(birth_date.month, birth_date.year)
        if months < 0:
            years -= 1
            months += 12