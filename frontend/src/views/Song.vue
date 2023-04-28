<template>
  <div class="p-8 flex flex-column gap-12">
    <div class="flex w-1/4 gap-8">
      <v-img :src="songData.image" class="rounded-lg w-1/2"></v-img>
      <div>
        <h1 class="text-4xl font-bold text-sky-900">{{ songData.title }}</h1>
        <h3 class="text-xl mt-2">{{ songData.artist }}</h3>
      </div>
    </div>
    <div class="flex flex columns-2 gap-64">
      <div>
        <h3 class="text-2xl font-bold mb-4">Original lyrics</h3>
        <p v-for="lyric in formattedLyrics">{{ lyric }}</p>
      </div>
      <div class="ml-20">
        <h3 class="text-2xl font-bold mb-4">Translated lyrics</h3>
        <p v-for="lyric in formattedLyrics">{{ lyric }}</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      songData: {
        id: 3,
        image:
          "https://i1.sndcdn.com/artworks-9wo2yVLSUwH72KIh-NdBfzQ-t500x500.jpg",
        artist: "Drake",
        title: "More M's",
        lyrics: `[Chorus]
Pullin' out the coupe at the lot
Told 'em fuck 12, fuck SWAT
Bustin' all the bells out the box
I just hit a lick with the box
Had to put the stick in the box, mmh
Pour up the whole damn seal, I'ma get lazy
I got the mojo deals, we been trappin' like the '80s
She sucked a nigga soul, gotta Cash App
Told 'em wipe a nigga nose, say slatt, slatt
I won't never sell my soul, and I can back that
And I really wanna know where you at, at
[Verse 1]
I was out back where the stash at
Cruise the city in a bulletproof Cadillac (Skrrt)
'Cause I know these niggas after where the bag at (Yeah)
Gotta move smarter, gotta move harder
Nigga try to get me for my water
I'll lay his ass down, on my son, on my daughter
I had the Draco with me, Dwayne Carter
Lotta niggas out here playin', ain't ballin'
I done put my whole arm in the rim, Vince Carter (Yeah)
And I know probably get a key for the quarter
Shawty barely seen in double C's, I bought 'em
Got a bitch that's looking like Aaliyah, she a model
I got the pink slip, all my whips is key-less
Compton, I'm about to get the key to the city
Patek like the sea, forgive me

[Chorus]
Pullin' out the coupe at the lot
Told 'em fuck 12, fuck SWAT
Bustin' all the bells out the box
I just hit a lick with the box
Had to put the stick in the box, mmh
Pour up the whole damn seal, I'ma get lazy
I got the mojo deals, we been trappin' like the '80s
She sucked a nigga soul, gotta Cash App
Told 'em wipe a nigga nose, say slatt, slatt
I won't never sell my soul, and I can back that
And I really wanna know where you at, at, hah
You might also like
HEATED
Beyoncé
Fingertips
Lana Del Rey
The Grants
Lana Del Rey
[Verse 2]
Hahaha, I been movin' 'em out
If Steelo with me, then he got the blues in the pouch (Yeah)
Took her to the forest, put the wood in her mouth
Bitch, don't wear no shoes in my house
The private I'm flyin' in, I never wan' fly again
I'll take my chances in traffic (Yeah)
She suckin' on dick, no hands with it
I just made the Rollie plain like a landing strip
I'm a 2020 president candidate
I done put a hundred bands on Zimmerman, shit
I been movin' real gangster, so that's why she picked a Crip
Shawty call me Crisco 'cause I pop my shit
Got it out the mud, there's nothin' you can tell me, yeah
When I had the drugs, I was street wealthy, yeah

[Chorus]
Pullin' out the coupe at the lot
Told 'em fuck 12, fuck SWAT
Bustin' all the bells out the box
I just hit a lick with the box
Had to put the stick in the box, mmh
Pour up the whole damn seal, I'ma get lazy
I got the mojo deals, we been trappin' like the '80s
She sucked a nigga soul, gotta Cash App
Told 'em wipe a nigga nose, say slatt, slatt
I won't never sell my soul, and I can back that
And I really wanna know where you at, at`,
      },
    };
  },
  computed: {
    formattedLyrics() {
      return this.songData.lyrics.split("\n");
    },
  },
};
</script>
