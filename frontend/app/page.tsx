import Link from "next/link";

export default function Home() {
  return (
    <main className="min-h-screen flex flex-col items-center justify-center gap-6 p-8">
      <h1 className="text-4xl font-bold">Course Organizer AI</h1>
      <p className="text-lg text-gray-600 text-center max-w-xl">
        An AI-powered study document organizer for students.
      </p>

      <Link
        href="/courses"
        className="px-6 py-3 rounded-xl bg-black text-white"
      >
        Create Course
      </Link>
    </main>
  );
}
