# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "canillas"
__date__ = "$25 mars 2015 16:57:05$"

import sys
import socket
import string
import os
import struct

#definir la fonction custom ici 

def x42(d,s):
    if (d != None): # je verifie que mon dicto n'est pas vide
        if 'act' in d: #je verifie que mon dictio est bien forme
            if (d['act'] == 'PRIVMSG'): # je check l'action est bien message
                
                if (d['src'][0] == '#'):  #si le message est sur un salon
                    
                    if(d['msg'] == "!0x42 "):
                        
                        message = "Bonne question ! " 
                        s.send("PRIVMSG #clubsecu %s \r\n" %(message))


def bite(d,s):
    if (d != None): # je verifie que mon dicto n'est pas vide
        if 'act' in d: #je verifie que mon dictio est bien forme
            if (d['act'] == 'PRIVMSG'): # je check l'action est bien message
                
                if (d['src'][0] == '#'):  #si le message est sur un salon
                    
                    if(d['msg'] == "!bite "):
                        
                        message = "Nomekrax say BITE it, just BITE it"
                        s.send("PRIVMSG #clubsecu %s \r\n" %(message))
                        
def Shellbash(d,s):
    if (d != None): # je verifie que mon dicto n'est pas vide
        if 'act' in d: #je verifie que mon dictio est bien forme
            if (d['act'] == 'PRIVMSG'): # je check l'action est bien message
                
                if (d['src'][0] == '#'):  #si le message est sur un salon
                    
                    if(d['msg'] == "!shellbash "):
                        
                        message = " \\bin\\sh = \\x31\\xc0\\x31\\xdb\\x31\\xc9\\x31\\xd2\\x52\\x68\\x6e\\x2f\\x73\\x68\\x68\\x2f\\x2f\\x62\\x69\\x89\\xe3\\x52\\x53\\x89\\xe1\\xb0\\x0b\\xcd\\x80 -29bytes" 
                        s.send("PRIVMSG #clubsecu %s \r\n" %(message))
                        
def LittleEndian(d,s):
    if (d != None): # je verifie que mon dicto n'est pas vide
        if 'act' in d: #je verifie que mon dictio est bien forme
            if (d['act'] == 'PRIVMSG'): # je check l'action est bien message
                
                if (d['src'][0] == '#'):  #si le message est sur un salon
                    msg1=d['msg'].split(" ")  #on decoupe 
                    #print(msg1)
                    #print(len(msg1))
                    if (msg1[0]=="!litendian"):  #ici pour modifier le mode de commande (ici !q)
                        #print(msg1[0])
                        if (len(msg1) == 3):
                            if (len(msg1[1])!=8):
                                #print("A")
                                message = "adresse incorrecte"
                            else:     
                                #print("B")
                                #print
                                message = "\\x"+msg1[1][6]+msg1[1][7]+"\\x"+msg1[1][4]+msg1[1][5]+"\\x"+msg1[1][2]+msg1[1][3]+"\\x"+msg1[1][0]+msg1[1][1]
                                message ="l'adresse en littleEndian de "+msg1[1]+" est "+message
                                #print message
                            
                            
                            s.send("PRIVMSG #clubsecu %s \r\n" %(message)) #je l'envoie dans le chan resir

        
def LittleEndian2(d,s):
    if (d != None): # je verifie que mon dicto n'est pas vide
        if 'act' in d: #je verifie que mon dictio est bien forme
            if (d['act'] == 'PRIVMSG'): # je check l'action est bien message
                
                if (d['src'][0] == '#'):  #si le message est sur un salon
                    msg1=d['msg'].split(" ")  #on decoupe 
                    #print(msg1)
                    #print(len(msg1))
                    if (msg1[0]=="!litendian2"):  #ici pour modifier le mode de commande (ici !q)
                        #print(msg1[0])
                        
                        if (len(msg1) == 3):
                          
                                    
                            #print("B")
                            
                            
                            if (string.octdigits.find(msg1[1][0]) == -1):
                                
                                message = "c'est quoi cette merde que tu essayes de me fourgué"
                            
                            elif(string.octdigits.find(msg1[1][1])== -1 and  msg1[1][1] !="x" and msg1[1][1] !="b"):  
                                
                                message = "c'est quoi cette merde que tu essayes de me fourgué"
                            
                            
                                
                                message = struct.pack("<I",int(msg1s),16).encode('string-escape') 
                            
                                message ="l'adresse en littleEndian de "+msg1[1]+" est "+message
                                #print message
                            
                            
                        s.send("PRIVMSG #resir %s \r\n" %(message)) #je l'envoie dans le chan resir


def readline(line,d): #ne gere que PING, PVMSG et JOIN
    
    message=""
    #je traite les  privmsg et les join et les ping FAIRE UN CASE SWITCH
    
    #ajout d un champ type toujours present pour faire du traitement sur les 
    #types d'action 
    
    # la taille du tableau est fixe je peux donc forger mon dictionnaire
    if (line[0]=="PING"):
        d = dict(id=0,usr ='serv',act='ping',src=line[1])
        return d 
    #la taille du tableau est variable     
    if (line[1]=="PRIVMSG"):
        user=line[0]
        action=line[1]
        source=line[2]
        #je recupere les informations "fixe" et je les enleve du tableau 
        line.pop(2)
        line.pop(1)
        line.pop(0)
        # je concatene tout le reste 
        for word in line:
            message = message+word+" "
        #j'enleve le premiere caractere ":" pour avoir un message parsable 
        message=string.lstrip(message,':')
        d=dict( id = 1,usr = user, act = action, src = source, msg = message)
        return d
    #la taille du tableau est fixe je peux donc forger mon dictionnaire
    if (line[1]=="JOIN"):
        d=dict(id=2,usr=line[0],act=line[1],whr=line[2])
        return d


def run():
    HOST="irc.clubsecu.fr"
    PORT=6667
    NICK="Robert-Bot" #a renommer 
    IDENT="BOT"
    REALNAME="Sp1p3-Bot"
    readbuffer=""    
    
    d=dict()
    s=socket.socket( )
    s.connect((HOST, PORT))
    s.send("NICK %s\r\n" % NICK)
    s.send("USER %s %s bla :%s\r\n" % (IDENT, HOST, REALNAME))
    
   
    #lecture du ficher contenant les membres du clubs secu et mise de ceux-ci dans un tableau 
    
    while 1:
        readbuffer=readbuffer+s.recv(1024)
        temp=string.split(readbuffer, "\n")
        readbuffer=temp.pop( )
        
        for line in temp:
            line=string.rstrip(line)
            line=string.split(line)

            if(line[0]=="PING"):
                s.send("PONG %s\r\n" % line[1])
            s.send("JOIN #clubsecu\r\n")
          
     
            d = readline(line, d)
            print(d)
#inserer la fonction custom ici
            bite(d,s)
            LittleEndian(d,s)
            LittleEndian2(d,s)
            Shellbash(d,s)
            x42(d,s)
           

if __name__ == "__main__":
   print(" Robert-Bot au Rapport")
   run()