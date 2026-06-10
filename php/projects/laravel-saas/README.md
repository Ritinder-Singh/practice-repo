# Laravel SaaS App — Multi-tenancy + Stripe + Livewire

## Setup

```bash
composer create-project laravel/laravel saas-app
cd saas-app
composer require laravel/sanctum stancl/tenancy livewire/livewire laravel/cashier
php artisan install:api
php artisan vendor:publish --tag=tenancy-config
```

## What to Build

### Milestone 1 — Auth (Sanctum)
- [ ] User model with email, name, role (admin/member)
- [ ] Login / register API endpoints
- [ ] `php artisan make:controller AuthController` — issue Sanctum tokens
- [ ] Protected routes with `auth:sanctum` middleware

### Milestone 2 — Multi-tenancy (stancl/tenancy)
- [ ] `Tenant` model: id, name, domain
- [ ] `TenantController` — create/switch tenant
- [ ] Database per tenant: `InitializeTenancyByDomain` middleware
- [ ] Central domain routes vs tenant routes

### Milestone 3 — Stripe Billing (Laravel Cashier)
- [ ] `User implements Billable` (Cashier trait)
- [ ] Subscription plans in `config/cashier.php`
- [ ] `POST /subscribe` — `$user->newSubscription('default', $priceId)->create($paymentMethodId)`
- [ ] Stripe webhooks: `php artisan cashier:webhook`, handle `invoice.payment_failed`

### Milestone 4 — Livewire Components
- [ ] `php artisan make:livewire Dashboard` — real-time stats
- [ ] `php artisan make:livewire DataTable` — searchable, paginated table
- [ ] `php artisan make:livewire BillingPortal` — upgrade/downgrade/cancel
- [ ] `wire:model`, `wire:click`, `wire:loading` directives

### Milestone 5 — Background Jobs
- [ ] `php artisan make:job SendWelcomeEmail`
- [ ] `php artisan make:job ProcessSubscriptionRenewal`
- [ ] Queue driver: Redis; Horizon for monitoring
- [ ] Schedule: `$schedule->job(new ProcessSubscriptionRenewal)->daily()`

### Milestone 6 — Testing
- [ ] Feature tests: `php artisan make:test SubscriptionTest`
- [ ] Mock Stripe with `Http::fake()`
- [ ] Database: `RefreshDatabase` trait

## Key Concepts Demonstrated

| Concept | Where |
|---------|-------|
| Sanctum token-based API authentication | `AuthController`, `auth:sanctum` middleware |
| Multi-tenancy with `stancl/tenancy` (database-per-tenant) | `Tenant` model, `InitializeTenancyByDomain` |
| Subdomain routing for tenant isolation | `routes/web.php` |
| Laravel Cashier Stripe subscription billing | `POST /subscribe`, `User implements Billable` |
| Stripe webhook handling (`invoice.payment_failed`) | Milestone 3 |
| Livewire reactive components (`wire:model`, `wire:click`) | `Dashboard`, `DataTable`, `BillingPortal` |
| Redis-backed queue jobs (Horizon monitoring) | `SendWelcomeEmail`, `ProcessSubscriptionRenewal` |
| Laravel scheduler (`$schedule->job()->daily()`) | Milestone 5 |
| Feature testing with `Http::fake()` for Stripe mocking | Milestone 6 |
