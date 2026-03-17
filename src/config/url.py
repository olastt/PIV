class Url:
    # VM: основной API (все запросы кроме логина)
    DOMAIN_VM_PROD = "https://mobilebackend.vetmanager.cloud"
    # DOMAIN_VM_TEST = "https://mobilebackend-test.kube-dev.vetmanager.cloud"

    # Логин идёт на отдельный хост; токен из ответа пишется в .env и используется для API выше
    DOMAIN_VM_AUTH = "https://devolesya.vetmanager2.ru"

    # ==================== AUTH ====================
    AUTH_BY_LOGIN_AND_PASSWORD = "/token_auth.php"

    # ==================== USERS ====================
    GET_USER_BY_ID = "/api/v2/users/{user_id}"
    PATCH_USER = "/api/v2/users/{user_id}"
    GET_USER_HOME = "/api/v2/users/{user_id}/home"
    GET_USER_SETTINGS_PAYMENT = "/api/v2/users/{user_id}/settings/payment"
    GET_USER_STORES = "/api/v2/users/{user_id}/stores"
    GET_USER_SCHEDULES = "/api/v2/users/{user_id}/schedules"
    GET_USER_ALLOWED_CLINICS = "/api/v2/users/{user_id}/allowedclinics"
    POST_USER_LOGOUT = "/api/v2/users/{user_id}/logout"
    GET_DOCTORS = "/api/v2/users/doctors"

    # ==================== CHECKVERSION ====================
    GET_CHECKVERSION = "/api/v2/checkversion"

    # ==================== CLINICS ====================
    GET_CLINICS = "/api/v2/clinics"
    GET_PROPERTIES = "/api/v2/properties"

    # ==================== CASSA ====================
    GET_CASSA_BY_USER = "/api/v2/cassa/{user_id}"

    # ==================== TARIFF ====================
    GET_TARIFF = "/api/v2/tariff"

    # ==================== BILLING ====================
    GET_BILLING_URL = "/api/v2/billingurl"

    # ==================== ROLES ====================
    GET_ROLE_BY_ID = "/api/v2/roles/{id_role}"

    # ==================== HOSPITAL ====================
    GET_HOSPITAL = "/api/v2/hospital"
    GET_HOSPITAL_BLOCKS = "/api/v2/hospital/blocks"
    GET_HOSPITAL_LIST_STATUSES = "/api/v2/hospital/liststatuses"
    GET_HOSPITAL_BY_ID = "/api/v2/hospital/{recordId}"

    # ==================== CLIENTS ====================
    GET_CLIENT_BY_ID = "/api/v2/clients/{client_id}"
    PATCH_CLIENT = "/api/v2/clients/{client_id}"
    GET_CLIENTS_SEARCH = "/api/v2/clients/search/"
    POST_CLIENTS = "/api/v2/clients"
    GET_CLIENT_PETS = "/api/v2/clients/{client_id}/pets"
    GET_CLIENT_INVOICES = "/api/v2/clients/{client_id}/invoices"

    # ==================== PETS ====================
    GET_PETS_TYPES = "/api/v2/pets/types"
    GET_PETS_GENDERS = "/api/v2/pets/genders"
    GET_BREEDS_BY_TYPE = "/api/v2/pets/types/{type_id}/breeds"
    GET_PETS_BREEDS = "/api/v2/pets/breeds"
    GET_PET_BY_CLIENT = "/api/v2/clients/{client_id}/pets/{pet_id}"

    # ==================== PRODUCTS ====================
    GET_PRODUCTS = "/api/v2/products"
    GET_PRODUCTS_CATEGORIES = "/api/v2/products/categories"
    GET_PRODUCT_BY_ID = "/api/v2/products/{product_id}"

    # ==================== ADMISSION ====================
    GET_ADMISSION_BY_ID = "/api/v2/users/admission/{admission_id}"
    GET_ADMISSIONS_BY_USER = "/api/v2/users/{user_id}/admission"

    # ==================== CALLS ====================
    GET_USER_CALLS = "/api/v2/users/{user_id}/calls"
    GET_CALLS_SEARCH = "/api/v2/calls/search"

    # ==================== COMBOMANUALS ====================
    GET_COMBOMANUALS_BY_ID = "/api/v2/combomanuals/{combomanuals_id}"
    GET_VACCINATION_TYPES = "/api/v2/combomanuals/vaccinationstypes"
    GET_REASONS_OF_VISIT = "/api/v2/combomanuals/reasonsofvisit"
    GET_CITIES = "/api/v2/combomanuals/cities"
    GET_TYPES_CITIES = "/api/v2/combomanuals/typescities"
    GET_STREETS_BY_CITY = "/api/v2/combomanuals/{city_id}/streets"
    GET_TYPES_STREETS = "/api/v2/combomanuals/typesstreets"

    # ==================== DIAGNOSES ====================
    GET_DIAGNOSES = "/api/v2/diagnoses"
    GET_DIAGNOS_BY_ID = "/api/v2/diagnoses/{diagnos_id}"

    # ==================== MEDICALCARDS ====================
    GET_DIAGNOSES_FOR_MEDICALCARDS = "/api/v2/clients/medicalcards/diagnoses"