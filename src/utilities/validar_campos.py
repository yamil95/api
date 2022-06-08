
import re
def validar_aux (ticket : dict):
    
           
      validar = lambda x: "ok" if re.sub ("[\w]+|[\d]+|[{}._:/,*°()\[\]\"\']+|[-]+","",str(x)).replace(" ","") == "" else "error"
      flag = map (lambda x :validar (x) if isinstance(x,dict) != True  else  validar(dict(x).values()) ,ticket.values() ) #json_dictionary.values()
      if "error" in flag:
          raise ValueError("ka një biletë të gabuar")
      else :
          return True
      
def validar_campos (lista_tickets: list):
    
    try:
        list (map (lambda x: x if validar_aux(x) != True else "",lista_tickets) )
        return "ok"
    
    except  Exception as e:
        
        return e
        
        