
// Exercise: Raffle Winner Verification Program

const winningParticipants = [
    { id: 'P001', name: 'Jennifer', ticketNumber: 'T001' },
    { id: 'P008', name: 'Michael', ticketNumber: 'T008' },
    { id: 'T015', name: 'Emily', ticketNumber: 'T015' },
    { id: 'T047', name: 'Charlie', ticketNumber: 'T047' }
  ]
  
  function findWinnerByName (name) {
    const winner = winningParticipants.find(participants => participants.name === name)
    return winner || 'No winner found with that name.' // Si no se cumple la condición, regresa el mensaje
  }
  
  function findIndexWinnerByTicket (ticketNumber) {
    const index = winningParticipants.findIndex(participants => participants.ticketNumber === ticketNumber)
    return index !== -1 ? index : 'No winner found with that ticket number.'
  }
  
  function displayWinnerInformation (winner) {
    if (winner !== undefined && winner != null && winner !== 'No winner found with that name.') {
      console.log('Winner information: ', winner)
    } else {
      console.log('No winner found.')
    }
  }

  
  const winnerByName = findWinnerByName('Emily')
  const indexWinnerByTicket = findIndexWinnerByTicket('T008')
  
  displayWinnerInformation(winnerByName)
  console.log('Index of Winner by Ticket Number: ', indexWinnerByTicket)

