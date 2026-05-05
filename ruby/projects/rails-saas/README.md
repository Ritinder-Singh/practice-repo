# Rails SaaS App — Devise + Stripe + Turbo

## Setup

```bash
rails new saas_app --database=postgresql --css=tailwind
cd saas_app
bundle add devise stripe turbo-rails stimulus-rails sidekiq acts_as_tenant
rails generate devise:install
rails generate devise User
rails db:create db:migrate
```

## What to Build

### Milestone 1 — Authentication (Devise)
- [ ] `User` model with Devise modules: :database_authenticatable, :registerable, :recoverable, :rememberable, :validatable
- [ ] Add `name`, `role` (enum: :member, :admin) columns to users
- [ ] Custom Devise views: `rails generate devise:views`
- [ ] `before_action :authenticate_user!` on protected controllers

### Milestone 2 — Multi-tenancy (acts_as_tenant)
- [ ] `Account` model: name, subdomain (unique), plan (enum: :free, :pro, :enterprise)
- [ ] `belongs_to :account` on User with `acts_as_tenant(:account)`
- [ ] Subdomain routing in `routes.rb`
- [ ] `ApplicationController`: `set_current_tenant_by_subdomain_or_domain`

### Milestone 3 — Stripe Billing
- [ ] `bundle add pay` (Pay gem for Stripe integration)
- [ ] `Subscription` model linked to Account
- [ ] Webhook endpoint for Stripe events (payment_intent.succeeded, customer.subscription.*)
- [ ] Billing portal: upgrade/downgrade plan, cancel subscription

### Milestone 4 — Real-time with Turbo Streams
- [ ] `Notification` model with `broadcasts_to` concern
- [ ] `<%= turbo_stream_from current_user %>` in layout
- [ ] After creating record, broadcast: `Turbo::StreamsChannel.broadcast_append_to(user, target: "notifications", partial: "...")`

### Milestone 5 — Background Jobs (Sidekiq)
- [ ] `config/sidekiq.yml`, `redis` adapter in `config/cable.yml`
- [ ] `WelcomeEmailJob < ApplicationJob` — sends email after signup
- [ ] `SubscriptionExpiryJob` — daily cron to check expired subscriptions
- [ ] Admin dashboard: `require 'sidekiq/web'`; mount behind admin auth

### Milestone 6 — Admin Panel
- [ ] `ActiveAdmin` or hand-built: list users, impersonate, manage accounts
- [ ] Metrics dashboard: total users, MRR, churn rate
