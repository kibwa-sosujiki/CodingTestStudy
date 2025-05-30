import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Calendar;
import java.util.Date;

class Solution {

    public String solution(String video_len, String pos, String op_start, String op_end, String[] commands) throws ParseException {
        SimpleDateFormat sdf = new SimpleDateFormat("mm:ss");

        Date videoLen = sdf.parse(video_len);
        Date position = sdf.parse(pos);
        Date opStart = sdf.parse(op_start);
        Date opEnd = sdf.parse(op_end);
        Date videoStart = sdf.parse("00:00");
        
        position = skipOp(position, opStart, opEnd);

        for (String command : commands) {
            if (command.equals("next")) {
                position = addSec(position, 10);
                if (position.compareTo(videoLen) >= 0) {
                    position = videoLen;
                }
            } else {
                position = addSec(position, -10);
                if (position.compareTo(videoStart) <= 0) {
                    position = videoStart;
                }
            }
            position = skipOp(position, opStart, opEnd);
        }
        return sdf.format(position);
    }

    private Date addSec(Date pos, int sec) {
        Calendar cal = Calendar.getInstance(); 
        cal.setTime(pos);
        cal.add(Calendar.SECOND, sec);
        return cal.getTime();
    }

    private Date skipOp(Date pos, Date opStart, Date opEnd) {
        if (pos.compareTo(opStart) >= 0 && pos.compareTo(opEnd) <= 0){
            return opEnd;
        };
        return pos;
    }
}
