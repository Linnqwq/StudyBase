export default function CoursesPage() {
  return (
    <main className="min-h-screen p-8">
      <h1 className="text-3xl font-bold">My Courses</h1>
      <p className="mt-4 text-gray-600">This is the courses page.</p>

      <div className="mt-8 space-y-4">
        <div className="rounded-xl border p-4">
          <h2 className="text-xl font-semibold">Sociology 3AC</h2>
          <p className="text-gray-500">Spring 2026</p>
        </div>

        <div className="rounded-xl border p-4">
          <h2 className="text-xl font-semibold">Econ 100A</h2>
          <p className="text-gray-500">Spring 2026</p>
        </div>
      </div>
    </main>
  );
}