# Accidental_Deaths
Readme

Personal data

Surnames: Mellado Díaz
Name: Luis


Project structure

Folder: Project 1
	Folder: data
		Accidental_deaths.xlxs : Contains the data used in the project.
	Folder: instructions
		instructions.txt: The instructions given by the teacher.
	Folder: src
		Function.py: A python file containing the read_data function definition.
		Function_test.py: A python file whose purpose is to test the previously                                                                                            mentioned read_data function
	Readme.md: This text file describing the project

Dataset description

My data set is called Accidental_deaths, it contains all the data about deaths due to gun accidents in Unite States from 2015 to 2016.
In this data set we can find the following information divided in columns:
Date: day, month and year of the accident (Data type str)
State: state where the accident took place (Data type str)
County: county or city of the state where the accident took place (Data type str)
Address: address of the place where the events occurred (Data type str)
Killed: number of people who died in the accident (Data type int)
Injured: number of non-fatally injured people (Data type int)
Operations: if there were any operation after the accident (Data type str)

Function description

The function read_data defined in function.py take as an input a file and return a list of tuples. The function is capable of reading the file Accidental_deaths.xlxs and classify its parameters (read_data  also work properly for other files with the same parameters).
Each tuple has all the seven parameters (date, state, county, address, killed, injured and operations) related to 1 of the 500 accidents in this data base. The function read_data could also work properly if the file given to it has the same parameters and extensions as Accidental_deaths.xlxs.
The function works using a cvs.reader and a namedtuple. The cvs.reader can distinguish one parameter of another when they are separated by a comma. With a for loop, we store every parameter o each accident in tuple. 
We are using a namedtuple because it makes things easier. In the future if we wanted to work with this database, it is more comfortable if we can refer to each parameter by its name. The namedtuple has the following shape:
Gunviolence = namedtuple(‘gunviolence’,’date,state,county,address,killed,injured,operations’)
