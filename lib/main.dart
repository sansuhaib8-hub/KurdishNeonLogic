import 'package:flutter/material.dart';

void main() {
  runApp(const KurdishNeonLogicApp());
}

class KurdishNeonLogicApp extends StatelessWidget {
  const KurdishNeonLogicApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      theme: ThemeData.dark().copyWith(
        scaffoldBackgroundColor: const Color(0xFF05050A),
        colorScheme: const ColorScheme.dark(
          primary: Color(0xFF00F0FF), // Neon Cyan
          secondary: Color(0xFFD300C5), // Neon Purple
        ),
      ),
      home: const MainGameScreen(),
    );
  }
}

class MainGameScreen extends StatelessWidget {
  const MainGameScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Container(
        decoration: const BoxDecoration(
          gradient: LinearGradient(
            begin: Alignment.topLeft,
            end: Alignment.bottomRight,
            colors: [Color(0xFF0A0A16), Color(0xFF05050A)],
          ),
        ),
        child: SafeArea(
          child: Padding(
            padding: const EdgeInsets.all(24.0),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.stretch,
              children: [
                // Header
                Row(
                  mainAxisAlignment: MainAxisAlignment.spaceBetween,
                  children: [
                    const Text(
                      'NEON LOGIC',
                      style: TextStyle(
                        fontSize: 28,
                        fontWeight: FontWeight.bold,
                        color: Color(0xFF00F0FF),
                        letterSpacing: 2,
                        shadows: [
                          Shadow(color: Color(0xFF00F0FF), blurRadius: 12),
                        ],
                      ),
                    ),
                    Container(
                      padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 6),
                      decoration: BoxDecoration(
                        border: Border.all(color: const Color(0xFFD300C5)),
                        borderRadius: BorderRadius.circular(20),
                      ),
                      child: const Text('SCORE: 00', style: TextStyle(color: Color(0xFFD300C5))),
                    ),
                  ],
                ),
                const SizedBox(height: 40),
                
                // Central Glassmorphism Game Board Mockup
                Expanded(
                  child: Container(
                    decoration: BoxDecoration(
                      color: Colors.white.withOpacity(0.03),
                      borderRadius: BorderRadius.circular(24),
                      border: Border.all(color: Colors.white.withOpacity(0.08)),
                    ),
                    child: Center(
                      child: Column(
                        mainAxisAlignment: MainAxisAlignment.center,
                        children: [
                          Icon(Icons.lock_open_rounded, size: 64, color: const Color(0xFF00F0FF).withOpacity(0.8)),
                          const SizedBox(height: 16),
                          Text(
                            'تۆڕی لۆجیکی ئامادەیە',
                            style: TextStyle(fontSize: 18, color: Colors.white.withOpacity(0.7)),
                          ),
                        ],
                      ),
                    ),
                  ),
                ),
                const SizedBox(height: 40),

                // Cyberpunk Core Button
                ElevatedButton(
                  style: ElevatedButton.styleFrom(
                    backgroundColor: const Color(0xFFD300C5),
                    padding: const EdgeInsets.symmetric(vertical: 16),
                    shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(12)),
                    shadowColor: const Color(0xFFD300C5),
                    elevation: 8,
                  ),
                  onPressed: () {},
                  child: const Text(
                    'دەستپێکردنی یاری',
                    style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold, color: Colors.white),
                  ),
                ),
              ],
            ),
          ),
        ),
      ),
    );
  }
}
