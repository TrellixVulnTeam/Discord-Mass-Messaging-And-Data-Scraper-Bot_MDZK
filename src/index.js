import 'dotenv/config'

import { Client } from "discord.js-selfbot-v13"
import Database from "easy-json-database"
import chalkAnimation from 'chalk-animation'
import { createSpinner } from "nanospinner"
import downapi from 'follow-redirects'
import fs from 'fs'
import uniqid from 'uniqid'

const { https } = downapi


const client = new Client({
    checkUpdate: false,
});

const sleep = (ms) => new Promise((resolve) => setTimeout(resolve, ms))


function download(url) {
    return new Promise((resolve, reject) => {
        https.get(url, (res) => {
            res.pipe(fs.createWriteStream(`src\\pfp\\${process.env.GUILDID}\\${uniqid()}.${process.env.FORMAT}`))
            .on('error', reject)
            .once('close', () => resolve(`src\\pfp\\${process.env.GUILDID}\\${uniqid()}.${process.env.FORMAT}`))
        })
    })
}

async function shuffle(sourceArray) {
    for (var i = 0; i < sourceArray.length - 1; i++) {
        var j = i + Math.floor(Math.random() * (sourceArray.length - i))
        var temp = sourceArray[j]
        sourceArray[j] = sourceArray[i]
        sourceArray[i] = temp
    }
    return sourceArray
}

async function files() {
    if (!fs.existsSync(`src\\database`)) {
        await fs.mkdirSync(`src\\database`)
    }

    if (!fs.existsSync(`src\\database\\${process.env.GUILDID}`)) {
     fs.mkdirSync(`src\\database\\${process.env.GUILDID}`)
    }

    if (!fs.existsSync(`src\\username`)) {
        await fs.mkdirSync(`src\\username`)
    }

    if (!fs.existsSync(`src\\username\\${process.env.GUILDID}`)) {
       await fs.mkdirSync(`src\\username\\${process.env.GUILDID}`)
    }


    await fs.createWriteStream(`src\\username\\${process.env.GUILDID}\\username.txt`, { overwrite: false })
    await sleep(500)
    fs.truncateSync(`src\\username\\${process.env.GUILDID}\\username.txt`, 0)
}


async function welcome() {
    console.log('==============================================')
    console.log('==============================================')
    console.log('==============================================')
    console.log('                                              ')
    console.log('		      Welcome                     ')
    console.log('                                              ')
    console.log('     Discord data scraping tool version 1.0.0')
    console.log('                                              ')
    console.log('==============================================')
    console.log('==============================================')
    console.log('==============================================')
    console.log('                               by Luka Mladenovic')
    var author = chalkAnimation.karaoke(`[Ready] Logged as ${client.user.tag}\n`)

    await sleep(2500)
    author.stop()
}

async function scrape() {
    const db = new Database(`./src/database/${process.env.GUILDID}/database.json`)
    var memberid =  await shuffle((await (await client.guilds.fetch(process.env.GUILDID)).members.fetch()).filter(x => x.user.id !== null && !x.user.bot).map(r => r.user.id))
    db.set('id', memberid )
    db.set('url', [])
    let l = memberid.length
    for (let i = 0; i < l; i++) {
        let spinner = createSpinner("Scraping...").start()
        let member = await client.users.fetch(memberid[i])
        

        fs.appendFileSync(`src\\username\\${process.env.GUILDID}\\username.txt`,  member.id+' | '+member.tag+'\r\n')

       
    }
    console.log('Database created.')
    console.log('Username files created.')
    console.log('Finished succesfully.')
    process.exit(0)
}

client.on('ready', async() => {
    await files()
    await welcome()
    scrape()
})


client.login(process.env.TOKEN)