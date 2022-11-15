import base64
import random
import string

def id_generator(size=6, chars=string.ascii_uppercase):
    return ''.join(random.choice(chars) for _ in range(size))
lista = ["SEX", "MYSEXPARTNER", "AH..", "ILOVEU", "IWANTSEXWITHU"]

def obfuscate(code):
    return_string = ""
    return_string += f'# Protected by 0x72\n\nimport base64\nimport os\nimport time\nimport random\n'
    code = """\n_0x72_IS_COOL_STRING_ = ''\ndef _0x72_PROTECTOR(_0x72_IS_COOL_):\n    global _0x72_IS_COOL_STRING_\n    if _0x72_IS_COOL_ != '_0x72_IS_COOL_':\n        _0x72_IS_COOL_STRING_ = f'{_0x72_IS_COOL_.decode("utf-16")}'\n        exec(u'\u0023\u0020\u0070\u0072\u006f\u0074\u0065\u0063\u0074\u0065\u0064\u0020\u0062\u0079\u0020\u0030\u0078\u0037\u0032')\n    else:\n        time.sleep(50000)\n        os._exit(0)"""
    return_string += f"{code}\n"
    numar = random.choice(range(20, 100))
    numar_random1 = random.choice(range(25, 100))
    numar1 = "_0x72_Protector_"+id_generator(numar)
    s = 0
    for each in range(0, 5):
        s+=1
        numar_ = random.choice(range(20, 100))
        numar2 = "_0x72_Protector_"+id_generator(numar_)
        coderob = f"# Protected by 0x72#1337 - {random.choice(lista)}   "*numar_
        coderob = base64.b64encode(bytes(coderob, 'utf-8')).decode('utf-8')
        return_string += f'try:\n    {numar2} = {coderob.encode("utf-16")}\n    _0x72_PROTECTOR({numar2})\n    exec(_0x72_IS_COOL_STRING_.strip())\nexcept Exception as e:\n    pass\n'
    return_string += f"\ntry:\n    {numar1} = {code.encode('utf-16')}\n    _0x72_PROTECTOR({numar1})\n    exec(_0x72_IS_COOL_STRING_.strip())\nexcept Exception as e:\n    pass\n"
    for each in range(0, 5):
        s+=1
        numar__ = random.choice(range(20, 100))
        numar3 = "_0x72_Protector_"+id_generator(numar__)
        coderob = f"# Protected by 0x72#1337 - {random.choice(lista)}   "*numar__
        coderob = base64.b64encode(bytes(coderob, 'utf-8')).decode('utf-8')
        return_string += f'try:\n    {numar3} = {coderob.encode("utf-16")}\n    _0x72_PROTECTOR({numar3})\n    exec(_0x72_IS_COOL_STRING_.strip())\nexcept Exception as e:\n    pass\n'
            
    return return_string
    
