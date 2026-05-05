// =============================================================================
// React / Next.js — Forms & Validation
// =============================================================================
// Topics: controlled components, uncontrolled (useRef), Server Actions,
//         react-hook-form, Zod validation, file uploads.
// Docs: https://react.dev/reference/react-dom/components/input
//       https://nextjs.org/docs/app/building-your-application/data-fetching/server-actions
// =============================================================================

// ─── CONTROLLED COMPONENTS ────────────────────────────────────────────────────

// TODO 1: Controlled input — every keystroke updates state
//   Build a LoginForm with email and password fields.
//   Validate on submit: email must contain @, password >= 8 chars.
//   Show inline error messages per field.
//
// function LoginForm() {
//   const [email, setEmail] = useState("");
//   const [password, setPassword] = useState("");
//   const [errors, setErrors] = useState<{ email?: string; password?: string }>({});
//
//   const validate = () => {
//     const errs: typeof errors = {};
//     if (!email.includes("@")) errs.email = "Invalid email";
//     if (password.length < 8) errs.password = "Min 8 characters";
//     return errs;
//   };
//
//   const handleSubmit = (e: React.FormEvent) => {
//     e.preventDefault();
//     const errs = validate();
//     if (Object.keys(errs).length > 0) { setErrors(errs); return; }
//     // submit...
//   };
// }

// TODO 2: Select, checkbox, radio — controlled pattern
//   Build a UserPreferencesForm with:
//   - <select> for theme (light | dark | system)
//   - <input type="checkbox"> for newsletter subscription
//   - <input type="radio"> group for notification frequency (never | daily | weekly)
//   Log the full form state on submit.

// TODO 3: Dynamic fields — add/remove
//   Build a TagInput where users can add custom tags and remove them:
//   - Text input + "Add" button appends a tag to an array
//   - Each tag has an × button to remove it
//   - Prevent duplicates, trim whitespace

// ─── NEXT.JS SERVER ACTIONS ───────────────────────────────────────────────────

// TODO 4: Server Action — form submission without JS
//   Server Actions run on the server — no API route needed.
//   The form works even with JS disabled (progressive enhancement).
//
// "use server";
// async function createUser(formData: FormData) {
//   const name = formData.get("name") as string;
//   const email = formData.get("email") as string;
//   // validate, save to DB
//   await db.user.create({ data: { name, email } });
//   revalidatePath("/users");
// }
//
// export default function NewUserForm() {
//   return (
//     <form action={createUser}>
//       <input name="name" type="text" required />
//       <input name="email" type="email" required />
//       <button type="submit">Create</button>
//     </form>
//   );
// }

// TODO 5: useFormState + useFormStatus — pending & error state
//   Add loading spinner and error feedback to the Server Action form above.
//
// "use client";
// import { useFormState, useFormStatus } from "react-dom";
//
// function SubmitButton() {
//   const { pending } = useFormStatus();
//   return <button type="submit" disabled={pending}>{pending ? "Saving..." : "Create"}</button>;
// }
//
// function NewUserFormWithFeedback() {
//   const [state, formAction] = useFormState(createUser, { error: null });
//   return (
//     <form action={formAction}>
//       {state.error && <p className="error">{state.error}</p>}
//       <input name="name" />
//       <input name="email" />
//       <SubmitButton />
//     </form>
//   );
// }

// TODO 6: File upload — controlled
//   Create a ProfilePictureUpload component:
//   - <input type="file" accept="image/*"> — show preview using URL.createObjectURL
//   - Validate: max 2MB, only jpeg/png/webp
//   - On submit, send via FormData to an API route (POST /api/upload)
//
// const handleFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
//   const file = e.target.files?.[0];
//   if (!file) return;
//   if (file.size > 2 * 1024 * 1024) { setError("Max 2MB"); return; }
//   const preview = URL.createObjectURL(file);
//   setPreviewUrl(preview);
//   return () => URL.revokeObjectURL(preview);  // cleanup!
// };
