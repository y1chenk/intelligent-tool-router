# Ledger versioning and extensions

Keep the ledger schema version separate from the plugin release version. A plugin wording or metadata update does not require a ledger migration.

## Compatibility policy

The ledger schema defines a frozen `0.2.x` core, starting at schema version `0.2.0`. This package's validator accepts `schema_version` values in that family with a nonnegative, non-zero-padded patch number. Freeze core property names, requiredness, types, enum values and meanings throughout that family. Keep `additionalProperties: false` on core objects to catch misspellings and unsupported fields.

Add optional data during 0.2.x only inside the reserved `extensions` object on the ledger, branch or evidence record. Use reverse-DNS-style keys such as `org.example.capture`; the namespace identifies the producer, not an independently verified source. Consumers must preserve unknown extension data when rewriting a ledger and ignore it when evaluating core state. An extension must not override core evidence, closure rules or authorization.

```json
{
  "schema_version": "0.2.1",
  "extensions": {
    "org.example.capture": {
      "retrieved_at": "2026-09-29T00:00:00Z"
    }
  }
}
```

This fragment demonstrates version and extension fields; it is not a complete valid ledger. The producer supplies actual observation values. Omit `extensions` when it adds no useful observable state. Never place credentials, unnecessary private details or hidden reasoning there.

Adding even an optional **core** field would be rejected by an older strict validator. Make any core shape or meaning change in a new minor version, such as 0.3.0, with an explicit migration and matching validator. Do not relabel an incompatible document as 0.2.x. Use the validator distributed in plugin 0.2.1 as the compatibility baseline; this contract does not assume that validators in earlier package previews accept extensions or later patch versions.

## Validation limits

Use a Draft 2020-12 JSON Schema validator and enable date/URI format checks explicitly where the implementation requires it. Structural acceptance proves neither factual accuracy, source independence nor correct transitions between saved states. The schema permits arbitrary extension values and does not validate their domain meaning; document and validate an extension separately when it matters to a task.
