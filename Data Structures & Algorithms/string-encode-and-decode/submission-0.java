class Solution {

    public String encode(List<String> strs) {
        StringBuilder str = new StringBuilder();
        for (String s :strs){
            int len = s.length();
            str.append(len);
            str.append("#");
            for (int i=0;i<len;i++)
            {
                char original_char = s.charAt(i);
                char result = (char)(original_char + 10);
                str.append(result);
            }
        }
         return str.toString();
    }

    public List<String> decode(String str) {
        List<String> result =  new ArrayList<>();
        int i = 0;
        while(i < str.length()){
            StringBuilder a = new StringBuilder();
            int hashindex = str.indexOf("#",i);
            String s = str.substring(i,hashindex);
            int len = Integer.parseInt(s);
            for (int j =hashindex+1;j<hashindex+1+len;j++)
            { 
                char encode_char = str.charAt(j);
                char r = (char)(encode_char - 10);
                a.append(r);
            }
            result.add(a.toString());
            i = hashindex + 1 + len; 

        }
        return result;
    }
}
