from db import clientPS

def productSchema(prod) ->dict:
    return {"id": str(prod[0]),
            "name":prod[1],
            "description":prod[2],
            "company":prod[3],
            "price": str(prod[4]),
            "units": str(prod[5]),
            "subcategory_id": prod[6]
        
    }
    
def consulta():
    try:
        conn=clientPS.client()
        
        cur=conn.cursor()
        
        cur.execute("select * from public.product")
        
        data= cur.fetchone()
    except Exception as e:
        print(f'Error connexió {e}')
    
    finally:
        conn.close
        return f"consulta {productSchema(data)}"

def consultaId(id:int):
    try: 
        conn=clientPS.client()
        
        cur=conn.cursor()
        
        cur.execute(f"select * from public.product where product_id={id}")
        
        data=cur.fetchone()
        
    except Exception as e:
        print (f'Error de connexió {e}')
    finally:
        conn.close
        return f"consulta {productSchema(data)}"

def insert(prod):
    try:
        conn=clientPS.client()
        
        cur=conn.cursor()
        
        cur.execute(f"""
                INSERT INTO public.product (product_id, name, description, company, price, units, subcategory_id, created_at, updated_at)
                VALUES ({prod.id},'{prod.name}','{prod.description}','{prod.company}',{prod.price},{prod.unit}, {prod.subcategory_id}, 'CURRENT_TIMESTAMP', 'CURRENT_TIMESTAMP' )
            """)
        
        conn.commit()
        
    except Exception as e:
        print(f'Error connexió {e}')
    
    finally:
        conn.close
        
    return {"message": "S'ha insertat correctament"}
