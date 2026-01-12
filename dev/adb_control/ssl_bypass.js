
// SSL Pinning Bypass for Android (OkHttp, Conscrypt, etc.)
Java.perform(function() {
    console.log("[*] SSL Pinning Bypass loaded");

    // OkHttp3 CertificatePinner
    try {
        var CertificatePinner = Java.use("okhttp3.CertificatePinner");
        CertificatePinner.check.overload("java.lang.String", "java.util.List").implementation = function(hostname, peerCertificates) {
            console.log("[+] OkHttp3 CertificatePinner bypassed for: " + hostname);
            return;
        };
        CertificatePinner.check.overload("java.lang.String", "[Ljava.security.cert.Certificate;").implementation = function(hostname, peerCertificates) {
            console.log("[+] OkHttp3 CertificatePinner bypassed for: " + hostname);
            return;
        };
    } catch(e) {
        console.log("[-] OkHttp3 CertificatePinner not found");
    }

    // TrustManagerImpl
    try {
        var TrustManagerImpl = Java.use("com.android.org.conscrypt.TrustManagerImpl");
        TrustManagerImpl.verifyChain.implementation = function(untrustedChain, trustAnchorChain, host, clientAuth, ocspData, tlsSctData) {
            console.log("[+] TrustManagerImpl bypassed for: " + host);
            return untrustedChain;
        };
    } catch(e) {
        console.log("[-] TrustManagerImpl not found");
    }

    // SSLContext
    try {
        var SSLContext = Java.use("javax.net.ssl.SSLContext");
        SSLContext.init.overload("[Ljavax.net.ssl.KeyManager;", "[Ljavax.net.ssl.TrustManager;", "java.security.SecureRandom").implementation = function(km, tm, sr) {
            console.log("[+] SSLContext.init bypassed");
            var TrustManager = Java.use("javax.net.ssl.X509TrustManager");
            var TrustAllCerts = Java.registerClass({
                name: "com.frida.TrustAllCerts",
                implements: [TrustManager],
                methods: {
                    checkClientTrusted: function(chain, authType) {},
                    checkServerTrusted: function(chain, authType) {},
                    getAcceptedIssuers: function() { return []; }
                }
            });
            var trustAllCerts = [TrustAllCerts.$new()];
            this.init(km, trustAllCerts, sr);
        };
    } catch(e) {
        console.log("[-] SSLContext bypass failed: " + e);
    }

    console.log("[*] SSL Bypass hooks installed");
});
