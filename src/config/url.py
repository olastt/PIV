class Url:
    # PIV: основной API мобильного приложения
    DOMAIN_PET_PROD = "https://petinvet.ru/api/v2"

    # Авторизация Vetmanager для получения token (POST getToken)
    DOMAIN_VM_AUTH = "https://devolesya.vetmanager2.ru/"

    # ==================== AUTH ====================
    AUTH_BY_LOGIN_AND_PASSWORD = "/token_auth.php"

    # ==================== PIV API ====================
    GET_API_KEY_BY_CLINIC_CODE = "/apiKey/byClinicCode"
    GET_CLIENT_BY_PHONE = "/clients/clientByPhone"
    GET_PHONE_PREFIX = "/getPhonePrefix"
    POST_SEND_SMS = "/sms/send"
    GET_SMS_CHECK = "/sms/check"
    GET_DOMAIN_NAME = "/domainName"
    GET_ADMISSIONS_BY_CLIENT_ID = "/admissions"
    GET_RECOMENDATIONS_BY_CLIENT_ID = "/medicalCards/recomendations"
    GET_VACCINATIONS_BY_CLIENT_ID = "/medicalCards/vaccinations"
    GET_CLINICS = "/clinics"
    GET_LAST_THREE_ARTICLES = "/articles/lastThree"
    GET_ARTICLES = "/articles"
    POST_EVENT = "/event"
    GET_DISCOUNT_CARDS = "/discountCard"
