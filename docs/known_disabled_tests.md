# Disabled Test Scenarios

These scenarios were found as commented-out code and were removed from test/runtime files before GitLab cleanup. They should stay as tracked work items instead of commented code.

## Clients

- `test_clients_combine`
- `ClientsStart.post_clients_combine`
- Reason: scenario needs stable data preparation for source client, target client, and target pet.

## Products

- `test_get_product_pricing`
- Earlier variants of `ProductsStart.get_product_pricing`
- Earlier variant of `ProductsStart.patch_product`
- Earlier variant of `ProductsStart.post_categories_products`
- Reason: expected statuses and required pricing/category data need to be clarified.

## Notification

- `test_post_notification_device`
- `test_post_vetmanager_hook`
- `NotificationStart.post_notification_device`
- `NotificationStart.post_vetmanager_hook`
- Reason: request data and backend behavior need confirmation before enabling in CI.

## Admission

- Earlier variants of `AdmissionStart.patch_admission`
- Earlier variant of `AdmissionStart.confirm_admission`
- Reason: current active implementations prepare data dynamically; old variants used stale static IDs and dates.

## Common

- Earlier variant of `CommonStart.get_redis_clear`
- Reason: Redis clear should remain guarded by explicit environment flag before running in CI.

## Medicalcards

- Earlier variant of `MedicalcardsStart.post_medicalcards_generate_llm`
- Reason: active implementation uses the current request body; old prompt-based variant needs backend confirmation.

## Invoice

- Earlier variant of `InvoiceStart.pay_invoice`
- Reason: payment payload and target invoice data need a stable CI-safe fixture.
