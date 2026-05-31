/**
 * Supabase Client Bridge for LWS Template Lab
 * Pre-filled with your public project details (LISA WOOD STUDIO WEBSITE bucket).
 * The anon key is safe to expose for public bucket reads.
 *
 * Now fully active for browsing + inserting real images into templates.
 */

const LWS_SUPABASE = {
  url: "https://aawnkxnnrymqbysgimqj.supabase.co",
  bucket: "LISA WOOD STUDIO WEBSITE",
  anonKey: ""
};

function getSupabaseKey() {
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
    async listImages(prefix = "", limit = 200) {
      const cleanPrefix = prefix.replace(/^\/+|\/+$/g, '');
      const url = `${LWS_SUPABASE.url}/storage/v1/object/list/${encodeURIComponent(LWS_SUPABASE.bucket)}?prefix=${encodeURIComponent(cleanPrefix)}&limit=${limit}&offset=0`;
      
      const res = await fetch(url, {
        headers: { 
          "Authorization": `Bearer ${key}`,
          "Content-Type": "application/json"
        }
      });
      
      if (!res.ok) {
        const text = await res.text().catch(() => '');
        throw new Error(`Supabase list failed (${res.status}): ${text || res.statusText}`);
      }
      return res.json();
    },

    getPublicUrl(path) {
      // Handles both with and without leading slash
      const cleanPath = path.replace(/^\/+/, '');
      return `${LWS_SUPABASE.url}/storage/v1/object/public/${encodeURIComponent(LWS_SUPABASE.bucket)}/${cleanPath}`;
    }
  };
}

window.LWS_SUPABASE = LWS_SUPABASE;
window.getSupabaseClient = getSupabaseClient;
window.getSupabaseKey = getSupabaseKey;
window.setSupabaseKey = setSupabaseKey;

console.log("%c[LWS Template Lab] Supabase bridge ACTIVE. Real image browsing enabled.", "color:#2a7");
