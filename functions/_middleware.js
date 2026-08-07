// Blocks private repo paths from ever being served by Cloudflare Pages.
// _redirects alone cannot do this: redirect rules do not shadow files that
// exist as static assets, so /dns/* was still downloadable. Pages Functions
// run before static asset serving, which makes this authoritative.
const PRIVATE_PATTERNS = [
  /^\/dns(\/|$)/i,
  /^\/docs(\/|$)/i,
  /^\/agents\.md$/i,
];

export async function onRequest({ request, next, env }) {
  const { pathname } = new URL(request.url);
  if (PRIVATE_PATTERNS.some((re) => re.test(pathname))) {
    const notFound = await env.ASSETS.fetch(new URL("/404.html", request.url));
    return new Response(notFound.body, {
      status: 404,
      headers: { "content-type": "text/html; charset=utf-8" },
    });
  }
  return next();
}
