import psycopg2
import streamlit as st

st.title("Sondage Ethic Fashion\n")
st.write("Veuillez saisir les informations demandées :")

# connexion
def create_connexion():
    URL = "postgres://nezir:S7WUsSJ2to8uIfHtpdAqriGDCeD1Hrxu@dpg-chd4qpm7avjcvo5maee0-a.frankfurt-postgres.render.com/data_fast_fashion"
    connexion = psycopg2.connect(URL)
    return connexion

def insert_data(data):
    connexion = create_connexion()
    cursor = connexion.cursor() 

    query = "INSERT INTO fashion (fast_influent, fast_frequency, fast_site, ethic_importance, ethic_select, ethic_price,recycling_constumer, recycling, environment, material, situation, sex, age) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    cursor.execute(query, data)

    connexion.commit()

    cursor.close()
    connexion.close()

def main():
    # fast fashion
    decision_options = ['Les prix bas', 'La variété des styles', 'La facilité d\'accès et la disponibilité dans les magasins', 'Les campagnes publicitaires', 'L\'influence des célébrités et des influenceurs']
    frequency_options = ['Plusieurs fois par mois', 'Une fois par mois', 'Moins souvent (quelques fois par an ou moins)']
    site_options = ["En ligne, sur internet", "En magasin : Dans les enseignes de mode fast fashion", "Marché temporaire ou magasins éphémères"]
   
    fast_influent = st.selectbox("Quels sont les facteurs qui influencent votre décision d'acheter des vêtements de la fast fashion ?", options =['']+ decision_options, format_func=str)
    if fast_influent is None:
        st.warning("Veuillez sélectionner une option valide.")
    fast_frequency = st.selectbox("À quelle fréquence achetez-vous des vêtements de fast fashion ?", options =['']+ frequency_options, format_func=str)
    if fast_frequency is None:
        st.warning("Veuillez sélectionner une option valide.")
    fast_site = st.selectbox("Où préférez-vous acheter vos vêtements de fast fashion ?", options=['']+site_options, format_func=str)
    if fast_site is None :
        st.warning("Veuillez sélectionner une option valide.")

    # Ethic fashion
    importance_options = ['Oui, toujours', 'Parfois, cela dépend de la situation', 'Non, cela ne fait pas partie de mes critères d\'achat']
    select_options = ['Conditions de travail équitables dans les usines de production', 'Utilisation de matériaux durables et respectueux de l\'environnement','Absence de travail des enfants dans la chaîne d\'approvisionnement', 'Transparence des pratiques commerciales et de la chaîne d\'approvisionnement', 'Soutien aux artisans locaux et aux communautés défavorisées']
    price_options = ['Oui, je suis prêt(e) à payer plus pour des vêtements éthiques', 'Non, je préfère les produits moins chers de la fast fashion', 'Cela dépend des circonstances et de la qualité du produit']
    
    ethic_importance = st.selectbox("Lorsque vous achetez des vêtements, accordez-vous de l'importance à l'éthique des marques de mode ?", options=['']+importance_options, format_func=str)
    if ethic_importance is None:
        st.warning("Veuillez sélectionner une option.")
    ethic_select = st.selectbox("Quels critères éthiques sont importants pour vous lors de l'achat de vêtements ?", options =['']+ select_options, format_func=str)
    if ethic_select is None :
        st.warning("Veuillez sélectionner une option valide.")
    ethic_price = st.selectbox("Seriez-vous prêt(e) à payer un prix plus élevé pour des vêtements éthiques et durables plutôt que d'opter pour des produits moins chers de la fast fashion ?", options=['']+price_options, format_func=str)
    if ethic_price is None:
        st.warning("Veuillez choisir une option valide.")

     # Ecologie
    recycling_options_constumer = ['Oui', 'Non', 'Par sûr']
    recycling_options = ['Donner des vêtements non utilisés à des organismes de bienfaisance ou les revendre', 'Réutiliser les vêtements en les combinant de différentes manières', 'Recycler les vêtements en les transformant en nouveaux produits']
    environment_options = ['Oui, je suis bien informé(e) sur les problématiques liées à la fast fashion', "J'en ai entendu parler, mais je ne suis pas très au courant des détails", "Non, je ne suis pas conscient(e) de l'impact de la fast fashion"]
    material_options = ['Non', 'Oui', 'Oui Certaines d\'entre elles', 'Je ne sais pas']
   
    recycling_constumer = st.selectbox("Êtes-vous conscient de l'importance du recyclage dans l'industrie de la mode ?", options = ['']+recycling_options_constumer, format_func=str)
    if recycling_constumer is None:
        st.warning("Veuillez choisir une option.")
    recycling = st.selectbox("Quelles actions de recyclage pratiquez-vous dans votre propre consommation de mode ?", options=[''] + recycling_options, format_func=str)
    if recycling is None:     
        st.warning("Veuillez choisir une option.")
    environment = st.selectbox("Êtes-vous conscient(e) de l'impact environnemental et social de la fast fashion ?", options=[''] + environment_options, format_func=str)
    if environment is None:
        st.warning("Veuillez sélectionner une option.")
    material = st.selectbox("Pensez-vous que les matières utilisées dans la fast fashion sont durables ?", options=[''] + material_options, format_func=str)
    if material is None:
        st.warning("Veuillez sélectionner une option.")

    # Identité Anonyme
    genre_options = ['Homme', 'Femme']
    situation_options = ['Étudiant(e)/Apprenti(e)', 'Salarié(e)', 'Retraité(e)', 'Autre']
    situation = st.selectbox("Situation socioprofessionnelle", options=[''] + situation_options, format_func=str)
    if situation is None:
        st.warning("Veuillez sélectionner une situation socioprofessionnelle.")
    age = st.number_input("Âge", min_value=0, max_value=130, value=18)
    if age is None:
        st.warning("Veuillez saisir un âge valide.")
    sex = st.selectbox("Genre", options=['']+genre_options, format_func=str)
    if sex is None:
        st.warning("Veuillez sélectionner un genre.")

    # Labels d'orientation
    st.write("\n---")
    st.write("Instructions :")
    st.write("- Assurez-vous de remplir tous les champs.")
    st.write("- Cliquez sur le bouton 'Envoyer' pour soumettre le formulaire.")
    # button d'envoie

    # button d'envoie
    if st.button("Envoyer"):
            # Sauvegarde des données dans la base de données
            data = (fast_influent, fast_frequency, fast_site, ethic_importance, ethic_select, ethic_price,recycling_constumer, recycling, environment, material, situation, sex, age)
            insert_data(data)
            st.write("\n---") 
            st.success("Données sauvegardées avec succès.\n Merci pour votre contribution !")




#appel à la methode main
if __name__ == '__main__':
    main()





