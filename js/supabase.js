/**
 * Supabase Client Bridge for LWS Template Lab
 * Pre-filled with your public project details (LISA WOOD STUDIO WEBSITE bucket).
 *
 * The anon key below is SAFE to expose in the browser: it is the public "anon"
 * key, and it is protected by Row Level Security. A scoped RLS policy allows
 * listing ONLY the art-project folders (artwork/, SURFACE SURVEYS/,
 * OMANI LANDSCAPES/). All other files in the bucket remain private.
 * NEVER put the secret "service_role" key in this file.
 *
 * Fully active for browsing + inserting real images into templates.
 */

const LWS_SUPABASE = {
  url: "https://aawnkxnnrymqbysgimqj.supabase.co",
  bucket: "LISA WOOD STUDIO WEBSITE",
  // Public anon key (RLS-protected, read/list only). Safe to ship to the browser.
  anonKey: "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImFhd25reG5ucnltcWJ5c2dpbXFqIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjQ2MDEwNTYsImV4cCI6MjA4MDE3NzA1Nn0.w7zFE-BYPBQKkf1wjHXQRnioVNf8pW9_smxmWu9eyKU"
};

function getSupabaseKey() {
  // Built-in key first, so the tool works on every page/origin with no setup.
  // A key manually saved via Settings is used only as a fallback.
  return LWS_SUPABASE.anonKey || localStorage.getItem('lws_supabase_anon_key') || '';
}

function setSupabaseKey(key) {
  if (key) {
    LWS_SUPABASE.anonKey = key;
    localStorage.setItem('lws_supabase_anon_key', key);
  }
}

/**
 * Returns a ready-to-use Supabase storage client or null if no key.
 */
function getSupabaseClient() {
  const key = getSupabaseKey();
  if (!key || key.length < 20) {
    return null;
  }
  LWS_SUPABASE.anonKey = key;

  return {
    async listImages(prefix = "", limit = 1000) {
      // Supabase Storage "list" is a POST with a JSON body (not a GET).
      // Keep a single trailing slash so the API returns the folder's CONTENTS.
      let cleanPrefix = prefix.replace(/^\/+/, '');
      if (cleanPrefix && !cleanPrefix.endsWith('/')) cleanPrefix += '/';
      const url = `${LWS_SUPABASE.url}/storage/v1/object/list/${encodeURIComponent(LWS_SUPABASE.bucket)}`;

      const res = await fetch(url, {
        method: "POST",
        headers: {
          "Authorization": `Bearer ${key}`,
          "apikey": key,
          "Content-Type": "application/json"
        },
        body: JSON.stringify({
          prefix: cleanPrefix,
          limit: limit,
          offset: 0,
          sortBy: { column: "name", order: "asc" }
        })
      });

      if (!res.ok) {
        const text = await res.text().catch(() => '');
        throw new Error(`Supabase list failed (${res.status}): ${text || res.statusText}`);
      }
      return res.json();
    },

    getPublicUrl(path) {
      // Encode each path segment so spaces / special characters resolve correctly.
      const cleanPath = String(path).replace(/^\/+/, '');
      const encodedPath = cleanPath.split('/').map(encodeURIComponent).join('/');
      return `${LWS_SUPABASE.url}/storage/v1/object/public/${encodeURIComponent(LWS_SUPABASE.bucket)}/${encodedPath}`;
    }
  };
}

window.LWS_SUPABASE = LWS_SUPABASE;
window.getSupabaseClient = getSupabaseClient;
window.getSupabaseKey = getSupabaseKey;
window.setSupabaseKey = setSupabaseKey;

console.log("%c[LWS Template Lab] Supabase bridge ACTIVE. Real image browsing enabled.", "color:#2a7");
