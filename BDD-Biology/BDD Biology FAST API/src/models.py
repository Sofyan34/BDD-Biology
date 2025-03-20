from sqlalchemy import Column, Integer, String, Date, Boolean, ForeignKey, Index, Numeric, Float,MetaData
from sqlalchemy.orm import relationship
from datetime import date
  
from src.database import Base

# classe permettant de définir les modèles de la base de données pour créer ou accéder aux tables
# hérite de la base définie dans database.py

# class Departement(Base):
# 	__tablename__ = "t_dept"

# 	code_dept = Column(String(2),primary_key=True)
# 	nom_dept = Column(String(50), default=None)
# 	ordre_aff_dept = Column(Integer, default=0)


# class Commune(Base):
# 	__tablename__ = "t_communes"

# 	id = Column(Integer,primary_key=True)
# 	dep = Column(String(2),ForeignKey('t_dept.code_dept'))
# 	cp = Column(String(5), default=None)
# 	ville = Column(String(50), default=None)

# 	__table_args__ = (Index('commune_index', "dep", "cp", "ville"),)

class classification(Base):
    __tablename__ = "t_spcent"

    codspc = Column(Integer, primary_key=True)
    genrespc = Column(String(8), default=None)
    nomspc = Column(String(40), default=None, index=True)
    prenomspc = Column(String(30), default=None)
    
    def __repr__(self): 
        return f"{self.codspc}, {self.nomspc}"



class informations(Base):
	__tablename__ = "t_entcde"

	codcde = Column(Integer,primary_key=True)
	datcde = Column(Date, default=date.today())
	codspc = Column(Integer,default=None)
	timbrespc = Column(Float, default=None)
	timbrecde = Column(Float, default=None)

# class Conditionnement(Base):
# 	__tablename__ = "t_conditionnement"

# 	idcondit = Column(Integer,primary_key=True)
# 	libcondit = Column(String(50), default=None)
# 	poidscondit = Column(Integer)
# 	prixcond = Column(Numeric, default=0.0000)
# 	ordreimp = Column(Integer)
# 	# codobj = Column(Integer, ForeignKey('t_objet.codobj'))
# 	objets = relationship("ObjetCond",back_populates='condit')


class repartition(Base):
    __tablename__ = "t_objet"

    codobj = Column(Integer, primary_key=True)
    libobj = Column(String(50), default=None)
    tailleobj = Column(String(50), default=None)
    puobj = Column(Numeric, default=0.0000)
    poidsobj = Column(Numeric, default=0.0000)


# class ObjetCond(Base):
# 	__tablename__ = "t_rel_cond"

# 	idrelcond = Column(Integer,primary_key=True, index=True)
# 	qteobjdeb = Column(Integer, default=0)
# 	qteobjfin = Column(Integer, default=0)
# 	codobj = Column(Integer, ForeignKey('t_objet.codobj'))
# 	codcond = Column(Integer, ForeignKey('t_conditionnement.idcondit'))
# 	objets = relationship("Objet",back_populates='condit')
# 	condit = relationship("Conditionnement",back_populates='objets')


class Detail(Base):
    __tablename__ = "t_dtlcode"

    id = Column(Integer, primary_key=True)
    Detailtext = Column(String, default=None)
 


# class DetailObjet(Base):
# 	__tablename__ = "t_dtlcode_codobj"

# 	id = Column(Integer,primary_key=True)
# 	detail_id = Column(Integer, ForeignKey('t_dtlcode.id'))
# 	objet_id = Column(Integer, ForeignKey('t_objet.codobj'))

# class Enseigne(Base):
# 	__tablename__ = "t_enseigne"

# 	id_enseigne = Column(Integer,primary_key=True)
# 	lb_enseigne = Column(String(50), default=None)
# 	ville_enseigne = Column(String(50), default=None)
# 	dept_enseigne = Column(Integer, default=0)


# class Poids(Base):
# 	__tablename__ = "t_poids"

# 	id = Column(Integer,primary_key=True)
# 	valmin = Column(Numeric, default=0)
# 	valtimbre = Column(Numeric, default=0)


# class Vignette(Base):
# 	__tablename__ = "t_poidsv"

# 	id = Column(Integer,primary_key=True)
# 	valmin = Column(Numeric, default=0)
# 	valtimbre = Column(Numeric, default=0)


# class Role(Base):
# 	__tablename__ = "t_role"

# 	codrole= Column(Integer,primary_key=True)
# 	librole = Column(String(25), default=None)


# class Utilisateur(Base):
# 	__tablename__ = "t_utilisateur"

# 	code_utilisateur = Column(Integer,primary_key=True)
# 	nom_utilisateur = Column(String(50), default=None)
# 	prenom_utilisateur = Column(String(50), default=None)
# 	username = Column(String(50), default=None)
# 	couleur_fond_utilisateur = Column(Integer, default=0)
# 	date_insc_utilisateur = Column(Date)


# class RoleUtilisateur(Base):
# 	__tablename__ = "t_utilisateur_role"

# 	id = Column(Integer,primary_key=True)
# 	utilisateur_id = Column(Integer, ForeignKey('t_utilisateur.code_utilisateur'))
# 	role_id = Column(Integer, ForeignKey('t_role.codrole'))