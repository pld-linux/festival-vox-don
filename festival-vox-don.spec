Summary:	British English male voice 'Donovan'
Summary(pl):	Brytyjska odmiana jêzyka angielskiego - g³os mêski 'Donovan'
Name:		festival-vox-don
Version:	0.1
Release:	1
License:	Distributable
Group:		Applications/Sound
Source0:	http://www.cstr.ed.ac.uk/download/festival/1.4.2/festvox_don.tar.gz
Requires:	festival-lex-OALD
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description


%prep
%setup -q -c %{name}-%{version}

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/festival/lib/voices/english

cd festival/lib/voices/english
cp -r don_diphone $RPM_BUILD_ROOT%{_datadir}/festival/lib/voices/english
rm $RPM_BUILD_ROOT%{_datadir}/festival/lib/voices/english/don_diphone/COPYING

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc festival/lib/voices/english/don_diphone/COPYING
%{_datadir}/festival/lib/voices/english/don_diphone
