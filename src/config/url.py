class Url:
    # VM: основной API (все запросы кроме логина)
    # DOMAIN_VM_PROD = "https://mobilebackend.vetmanager.cloud"
    DOMAIN_VM_TEST = "https://mobilebackend-test.kube-dev.vetmanager.cloud"

    # Логин идёт на отдельный хост; токен из ответа пишется в .env и используется для API выше
    DOMAIN_VM_AUTH = "https://three.test.kube-dev.vetmanager.cloud/"

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
    PATCH_USER_SETTINGS_PAYMENT = "/api/v2/users/settings/payment/{record_id}"
    POST_USER_SETTINGS_PAYMENT_CREATE = "/api/v2/users/settings/payment/0"

    # ==================== SETTINGS / SERVICE ====================
    GET_REDIS_CLEAR = "/api/v2/redis/clear"

    # ==================== CHECKVERSION ====================
    GET_CHECKVERSION = "/api/v2/checkversion"

    # ==================== CLINICS ====================
    GET_CLINICS = "/api/v2/clinics"
    GET_PROPERTIES = "/api/v2/properties"

    # ==================== CASSA ====================
    GET_CASSA_BY_USER = "/api/v2/cassa/{user_id}"

    # ==================== BILLING ====================
    GET_BILLING_URL = "/api/v2/billingurl"
    GET_TARIFF = "/api/v2/tariff"

    # ==================== ROLES ====================
    GET_ROLE_BY_ID = "/api/v2/roles/{id_role}"

    # ==================== HOSPITAL ====================
    GET_HOSPITAL = "/api/v2/hospital"
    GET_HOSPITAL_BLOCKS = "/api/v2/hospital/blocks"
    GET_HOSPITAL_LIST_STATUSES = "/api/v2/hospital/liststatuses"
    GET_HOSPITAL_BY_ID = "/api/v2/hospital/{recordId}"
    PATCH_HOSPITAL_BY_ID = "/api/v2/hospital/{recordId}"

    # ==================== CLIENTS ====================
    GET_CLIENT_BY_ID = "/api/v2/clients/{client_id}"
    PATCH_CLIENT = "/api/v2/clients/{client_id}"
    GET_CLIENTS_SEARCH = "/api/v2/clients/search/"
    POST_CLIENTS = "/api/v2/clients"
    GET_CLIENT_PETS = "/api/v2/clients/{client_id}/pets"
    GET_CLIENT_PET_BY_ID = "/api/v2/clients/{client_id}/pets/{pet_id}"
    GET_CLIENT_INVOICES = "/api/v2/clients/{client_id}/invoices"
    GET_CLIENT_INVOICE_PRODUCTS = "/api/v2/clients/{client_id}/invoices/{invoice_id}/products"
    POST_CLIENT_PAYMENTS = "/api/v2/clients/{client_id}/payments"
    GET_CLIENT_MATCH = "/api/v2/clients/{client_id}/match/"
    GET_CLIENT_CONTACTS = "/api/v2/clients/{client_id}/contacts"
    POST_CLIENTS_COMBINE = "/api/v2/clients/combine"

    # ==================== PETS ====================
    GET_PETS_TYPES = "/api/v2/pets/types"
    GET_PETS_GENDERS = "/api/v2/pets/genders"
    GET_BREEDS_BY_TYPE = "/api/v2/pets/types/{type_id}/breeds"
    GET_PETS_BREEDS = "/api/v2/pets/breeds"
    GET_PET_BY_CLIENT = "/api/v2/clients/{client_id}/pets/{pet_id}"
    POST_CLIENT_PET = "/api/v1/clients/{client_id}/pets"
    PATCH_CLIENT_PET = "/api/v2/clients/{client_id}/pets/{pet_id}"

    # ==================== PRODUCTS ====================
    GET_PRODUCTS = "/api/v2/products"
    GET_PRODUCTS_CATEGORIES = "/api/v2/products/categories"
    GET_PRODUCT_BY_ID = "/api/v2/products/{product_id}"
    GET_PRODUCT_STOCKBALANCES = "/api/v2/products/{product_id}/stockbalances"
    GET_PRODUCT_PRICING = "/api/v2/products/{product_id}/pricing/{qty}"
    GET_PRODUCTS_VACCINES = "/api/v2/products/vaccines"
    POST_PRODUCTS = "/api/v2/products"
    PATCH_PRODUCT = "/api/v2/products/{product_id}"
    DELETE_PRODUCTS = "/api/v2/products"
    GET_CATEGORIES_PRODUCTS = "/api/v2/categoriesproducts"
    GET_PRODUCTS_CATEGORIES_PRODUCTS = "/api/v2/products/categoriesproducts"
    DELETE_CATEGORIES_PRODUCTS = "/api/v2/categoriesproducts"
    POST_CATEGORIES_PRODUCTS = "/api/v2/categoriesproducts"
    PATCH_CATEGORIES_PRODUCTS = "/api/v2/categoriesproducts/{category_id}"

    # ==================== NOTIFICATION ====================
    POST_NOTIFICATION_DEVICE = "/api/v2/notification/device"
    GET_NOTIFICATION_SETTINGS = "/api/v2/notification/settings"
    POST_VETMANAGER_HOOK = "/api/v2/vetmanager-hook"
    DELETE_REMOVE_NOTIFICATION = "/api/v2/remove-notification/{notification_id}"
    PATCH_NOTIFICATION_SETTINGS = "/api/v2/notification/settings"

    # ==================== ADMISSION ====================
    GET_ADMISSION_BY_ID = "/api/v2/users/admission/{admission_id}"
    GET_ADMISSIONS_BY_USER = "/api/v2/users/{user_id}/admission"
    POST_CREATE_ADMISSION = "/api/v2/users/{user_id}/admission"
    PATCH_USER_ADMISSION = "/api/v2/users/{user_id}/admission/{admission_id}"
    POST_ADMISSION_CONFIRM = "/api/v2/users/admission/{admission_id}/confirm"

    # ==================== INVOICE ====================
    POST_CLIENT_INVOICES = "/api/v2/clients/{client_id}/invoices"

    # ==================== CALLS ====================
    GET_USER_CALLS = "/api/v2/users/{user_id}/calls"
    GET_CALLS_SEARCH = "/api/v2/calls/search"
    POST_CREATE_USER_CALL = "/api/v2/users/{user_id}/calls"
    PUT_UPDATE_USER_CALL = "/api/v2/users/{user_id}/calls/{call_id}"
    GET_USER_CALL_BY_ID = "/api/v2/users/{user_id}/calls/{call_id}"

    # ==================== COMBOMANUALS ====================
    GET_COMBOMANUALS_BY_ID = "/api/v2/combomanuals/{combomanuals_id}"
    GET_VACCINATION_TYPES = "/api/v2/combomanuals/vaccinationstypes"
    GET_REASONS_OF_VISIT = "/api/v2/combomanuals/reasonsofvisit"
    GET_RESULT_OF_VISIT = "/api/v1/combomanuals/resultofvisit"
    GET_CITIES = "/api/v2/combomanuals/cities"
    GET_TYPES_CITIES = "/api/v2/combomanuals/typescities"
    GET_STREETS_BY_CITY = "/api/v2/combomanuals/{city_id}/streets"
    GET_TYPES_STREETS = "/api/v2/combomanuals/typesstreets"
    POST_STREETS = "/api/v2/combomanuals/streets"
    POST_CITIES = "/api/v2/combomanuals/cities"

    # ==================== DIAGNOSES ====================
    GET_DIAGNOSES = "/api/v2/diagnoses"
    GET_DIAGNOS_BY_ID = "/api/v2/diagnoses/{diagnos_id}"
    POST_DIAGNOSES = "/api/v2/diagnoses"
    PATCH_DIAGNOS = "/api/v2/diagnoses/{diagnos_id}"
    DELETE_DIAGNOS = "/api/v2/diagnoses/{diagnos_id}"

    # ==================== MEDICALCARDS ====================
    GET_DIAGNOSES_FOR_MEDICALCARDS = "/api/v2/clients/medicalcards/diagnoses"
    GET_VACCINATIONS_BY_PET = "/api/v2/medicalcards/vaccinations/{pet_id}"
    POST_MEDICALCARD_VACCINATION = "/api/v2/medicalcards/{medicalcard_id}/vaccinations/{pet_id}"
    PATCH_MEDICALCARD_VACCINATION = "/api/v2/medicalcards/{medicalcard_id}/vaccinations/{vaccination_id}"
    PATCH_MEDICALCARD_VACCINATION_SHORT = "/api/v1/medicalcards/vaccinations/{vaccination_id}"
    GET_MEDICALCARDS_BY_CLIENT = "/api/v2/clients/{client_id}/medicalcards"
    GET_MEDICALCARD_BY_CLIENT = "/api/v2/clients/{client_id}/medicalcards/{medicalcard_id}"
    GET_MEDICALCARD_TEXT_TEMPLATES = "/api/v2/medicalcards/texttemplates"
    GET_MEDICALCARDS_HISTORY = "/api/v2/clients/{client_id}/medicalcards/history"
    POST_MEDICALCARDS_UPLOADFILES = "/api/v2/medicalcards/uploadfiles"
    POST_MEDICALCARDS_GENERATE_LLM = "/api/v2/medicalcards/generate-llm"
    POST_CREATE_MEDICALCARD = "/api/v2/clients/{client_id}/medicalcards"
    PATCH_MEDICALCARD = "/api/v2/clients/{client_id}/medicalcards/{medicalcard_id}"
